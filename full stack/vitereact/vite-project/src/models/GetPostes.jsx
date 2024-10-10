import React, { useState, useEffect } from "react";
import ShowAll from "../components/ShowAll";

const GetPostes = () => {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filterId, setFilterId] = useState("");
  const [sortOrder, setSortOrder] = useState("asc");
  const [sortByIdOrder, setSortByIdOrder] = useState("asc");

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await fetch("https://jsonplaceholder.typicode.com/posts");
        const data = await response.json();
        setPosts(data);
      } catch (error) {
        console.error("Error fetching posts:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, []);

  if (loading) {
    return <div className="d-flex justify-content-center"><div className="spinner-border" role="status"><span className="visually-hidden">Loading...</span></div></div>;
  }

  const filteredPosts = posts.filter((post) => filterId === "" || post.id.toString() === filterId);
  
  const finalSortedPosts = [...filteredPosts].sort((a, b) => sortOrder === "asc" ? a.title.localeCompare(b.title) : b.title.localeCompare(a.title));

  return (
    <div className="container mt-4">
      <h1 className="mb-4">Blog Posts</h1>
      <div className="row g-3 mb-4">
        <div className="col-md-4">
          <input
            type="text"
            className="form-control"
            placeholder="Filter by ID"
            value={filterId}
            onChange={(e) => setFilterId(e.target.value)}
          />
        </div>
        
        <div className="col-md-4">
          <select className="form-select" value={sortOrder} onChange={(e) => setSortOrder(e.target.value)}>
            <option value="asc">Sort by Title A-Z</option>
            <option value="desc">Sort by Title Z-A</option>
          </select>
        </div>
      </div>
      
      <ShowAll posts={finalSortedPosts} />
    </div>
  );
};

export default GetPostes;
import ShowPost from "./ShowPost"
import React from "react"

const ShowAll = ({posts}) => {
  return (
    <div className="table-responsive">
      <table className="table table-striped table-hover">
        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Body</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {posts.map((post) => (
            <ShowPost key={post.id} postId={post.id} title={post.title} body={post.body} />
          ))} 
        </tbody>
      </table>
    </div>
  );
};

export default ShowAll;
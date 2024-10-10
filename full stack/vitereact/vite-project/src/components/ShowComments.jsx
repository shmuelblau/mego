import React, { useState, useEffect } from "react";

const ShowComments = ({ postId }) => {
    const [comments, setComments] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchComments = async () => {
            try {
                const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${postId}/comments`);
                const data = await response.json();
                setComments(data);
            } catch (error) {
                console.error("Error fetching comments:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchComments();
    }, [postId]);

    if (loading) {
        return <p className="text-center">טוען תגובות...</p>;
    }

    return (
        <div className="comments-container">
            <ul className="list-group">
                {comments.map(comment => (
                    <li key={comment.id} className="list-group-item">
                        <h5 className="mb-1">{comment.name}</h5>
                        <p className="mb-1">{comment.body}</p>
                        <small className="text-muted">{comment.email}</small>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ShowComments;
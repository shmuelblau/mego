import React, { useState } from "react";
import ShowComments from "./ShowComments";

const ShowPost = ({postId, title, body}) => {
    const [isModalOpen, setIsModalOpen] = useState(false);

    const openModal = () => setIsModalOpen(true);
    const closeModal = () => setIsModalOpen(false);

    return (
        <>
            <tr>
                <td>{postId}</td>
                <td>{title}</td>
                <td>{body.substring(0, 100)}...</td>
                <td>
                    <button className="btn btn-primary btn-sm" onClick={openModal}>הצג תגובות</button>
                </td>
            </tr>
            {isModalOpen && (
                <div className="modal fade show" tabIndex="-1" style={{display: 'block'}}>
                    <div className="modal-dialog modal-lg">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title">תגובות לפוסט {postId}</h5>
                                <button type="button" className="btn-close" onClick={closeModal}></button>
                            </div>
                            <div className="modal-body">
                                <h6 className="mb-3">{title}</h6>
                                <p>{body}</p>
                                <hr />
                                <ShowComments postId={postId} />
                            </div>
                            <div className="modal-footer">
                                <button type="button" className="btn btn-secondary" onClick={closeModal}>סגור</button>
                            </div>
                        </div>
                    </div>
                </div>
            )}
            {isModalOpen && <div className="modal-backdrop fade show"></div>}
        </>
    );
};

export default ShowPost;
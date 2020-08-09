import express from "express";
import routes from "../routes";
import {
  videos,
  upload,
  editVideo,
  deleteVideo,
} from "../controllers/videoController";

const videoRouter = express.Router();

videoRouter.get(routes.home, videos);
videoRouter.get(routes.upload, upload);
videoRouter.get(routes.videoDetail, (req, res) => res.send("videoDetail"));
videoRouter.get(routes.editVideo, editVideo);
videoRouter.get(routes.deleteVideo, deleteVideo);

export default videoRouter;

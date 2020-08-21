import express from "express";
import routes from "../routes";
import {
  deleteVideo,
  videoDetail,
  getUpload,
  postUpload,
  getEditVideo,
  postEditVideo,
} from "../controllers/videoController";
import { uploadVideo, onlyPublic } from "../middlewares";

const videoRouter = express.Router();

videoRouter.get(routes.upload, onlyPublic, getUpload);
videoRouter.post(routes.upload, uploadVideo, onlyPublic, postUpload);

videoRouter.get(routes.videoDetail(), videoDetail);

videoRouter.get(routes.editVideo(), onlyPublic, getEditVideo);
videoRouter.post(routes.editVideo(), onlyPublic, postEditVideo);

videoRouter.get(routes.deleteVideo(), onlyPublic, deleteVideo);

export default videoRouter;

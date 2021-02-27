import pyscreenrec


class screeRecording:
    SC = pyscreenrec.ScreenRecorder()

    def recording(self, uname="kamabay"):
        screeRecording().SC.start_recording(str(uname)+".mp4")

    def stopRecord(self):
        screeRecording().SC.stop_recording()

    def pauseRecord(self):
        screeRecording().SC.pause_recording()

    def resumeRecord(self):
        screeRecording().SC.resume_recording()

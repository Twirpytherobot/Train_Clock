from samplebase import SampleBase
import math
import random
import time


    
class TrainClock(SampleBase):
    def __init__(self, *args, **kwargs):
        super(TrainClock, self).__init__(*args, **kwargs)
        
        
    def Track_Circle(self,r,xpos,ypos,n=172):
        track = [(round(math.cos(2*self.pi/n*x)*r)+xpos,round(math.sin(2*self.pi/n*x)*r)+ypos) for x in range(0,n+1)]
        return track
    
    def Render_Track(self,track):
        for sleeper in range(len(track)):
            self.offset_canvas.SetPixel(track[sleeper][0],track[sleeper][1], 50, 0 , 50)
            
        return  
    def Render_Station(self,track,num_station):
    
        stations = math.floor((len(track))/num_station)
        station_spacing = 0
        for i in range(num_station):
            
            
            if station_spacing >= len(track):
                break
            self.offset_canvas.SetPixel(track[station_spacing-2][0],track[station_spacing-2][1], 255, 0 , 50)
            self.offset_canvas.SetPixel(track[station_spacing-1][0],track[station_spacing-1][1], 255, 0 , 50)
            self.offset_canvas.SetPixel(track[station_spacing][0],track[station_spacing][1], 255, 0 , 50)
            station_spacing = station_spacing + stations
    def Draw_Screen(self):
        self.offset_canvas = self.matrix.SwapOnVSync(self.offset_canvas)
        return self.offset_canvas
    
    def Render_Train(self,length,track,tick):
        
        
        self.offset_canvas.SetPixel(track[tick-2][0],track[tick-2][1], 0, 255 , 0)
        self.offset_canvas.SetPixel(track[tick-1][0],track[tick-1][1], 0, 255 , 0)
        self.offset_canvas.SetPixel(track[tick][0],track[tick][1], 0, 255 , 0)
        
        if length > 1:
            
            for i in range(length):
                x=4*i    
                self.offset_canvas.SetPixel(track[tick-6-x][0],track[tick-6-x][1], 255, 255 , 0)
                self.offset_canvas.SetPixel(track[tick-5-x][0],track[tick-5-x][1], 255, 255 , 0)
                self.offset_canvas.SetPixel(track[tick-4-x][0],track[tick-4-x][1], 255, 255 , 0)
        
        
        return
    
    def run(self):
        self.pi = math.pi
        self.offset_canvas = self.matrix.CreateFrameCanvas()
        self.cent_x = self.matrix.width / 2
        self.cent_y = self.matrix.height / 2
        self.hour_track = self.Track_Circle(27,31,31)
        print(len(self.hour_track))
        
        self.minute_track = self.Track_Circle(23,31,31)
        print(len(self.minute_track))
        while True:
            
            self.Render_Track(self.hour_track)
            self.Render_Track(self.minute_track)
            self.Render_Station(self.hour_track,12)
            self.Render_Station(self.minute_track,12)
            
            self.Render_Train(3,self.hour_track,1)
            self.Draw_Screen()
            
            
            
#             for j in range(len(hour_track)):
#                 offset_canvas.Clear()
#                 for i in hour_track:
#             
#                     offset_canvas.SetPixel(i[0],i[1], 50, 0 , 50)
#                 
#                     for k in range(len(minute_track)):
#                         for l in minute_track:
#             
#                             offset_canvas.SetPixel(l[0],l[1], 50, 0 , 50)
#                         offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
#                 if j < len(hour_track):
#                     offset_canvas.SetPixel(hour_track[j][0],hour_track[j][1], 50, 0, 50)
#                     offset_canvas.SetPixel(hour_track[j-1][0],hour_track[j-1][1], 0, 255 , 0)
#                     offset_canvas.SetPixel(hour_track[j-2][0],hour_track[j-2][1], 0, 255 , 0)
#                     offset_canvas.SetPixel(hour_track[j-3][0],hour_track[j-3][1], 0, 255 , 0)
#                     offset_canvas.SetPixel(hour_track[j-4][0],hour_track[j-4][1], 0, 255 , 0)
#                     
#                     offset_canvas.SetPixel(hour_track[j-5][0],hour_track[j-5][1], 50, 0, 50)
#                     offset_canvas.SetPixel(hour_track[j-6][0],hour_track[j-6][1], 255, 255 , 0)
#                     offset_canvas.SetPixel(hour_track[j-7][0],hour_track[j-7][1], 255, 255 , 0)
#                     offset_canvas.SetPixel(hour_track[j-8][0],hour_track[j-8][1], 255, 255 , 0)
#                     offset_canvas.SetPixel(hour_track[j-9][0],hour_track[j-9][1], 255, 255 , 0)
#                     
#                     offset_canvas.SetPixel(hour_track[j-10][0],hour_track[j-10][1], 50, 0, 50)
#                     offset_canvas.SetPixel(hour_track[j-11][0],hour_track[j-11][1], 255, 255 , 0)
#                     offset_canvas.SetPixel(hour_track[j-12][0],hour_track[j-12][1], 255, 255 , 0)
#                     offset_canvas.SetPixel(hour_track[j-13][0],hour_track[j-13][1], 255, 255 , 0)
#                     offset_canvas.SetPixel(hour_track[j-14][0],hour_track[j-14][1], 255, 255 , 0)
#                     
#                     
#                     
#                     offset_canvas = self.matrix.SwapOnVSync(offset_canvas)
#                     #time.sleep(0.05)
#                 else:
#                     break
# Main function
if __name__ == "__main__":
    train_clock = TrainClock()
    if (not train_clock.process()):
        train_clock.print_help()
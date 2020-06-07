Java.perform(function () {
    var res = Java.use("com.example.touchgame.ResultActivity");
   
    res.onStart.implementation = function()
    {
        for(var i = 500;i<=999;i++)
        {
            var t = this.Convertkey1(i);
            t = this.Convertkey2(t);
            t = this.Convertkey3(t);
            t = this.Convertkey4(t);
            t = this.Convertkey5(t);
            t = this.Convertkey6(t);
            t = this.Convertkey7(t);
            console.log(t);
        }
        return ret;
    }
}
    
);
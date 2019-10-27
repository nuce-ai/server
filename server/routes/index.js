var express = require('express');
var router = express.Router();
var Python = require('python-shell');
const fs = require('fs'); 
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
const inputFilePath = 'E:/nuce-ai/server/tensorflow/test.json'

router.post('/',(req,res,next)=>{

    const pathApp = 'E:/nuce-ai/Tensorflow/models/research/object_detection/lab.py'
    Python.PythonShell.run(pathApp,null,(err,results)=>{
      if(err) res.sendStatus(404);
      if(typeof(results) === 'object') res.send('success');
     })
     
  })

  

router.get('/get/object',(req,res,next)=>{
   if(fs.existsSync(inputFilePath)){

   }
    fs.readFile(inputFilePath,(err,result)=>{
      if(err) console.log(err);
      if(typeof(result) === 'undefined'){
        res.send("Not data")
      }
      else{
        res.send(JSON.parse(result))
      }
    
    })
})

module.exports = router;

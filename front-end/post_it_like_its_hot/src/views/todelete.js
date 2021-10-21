const myDataObject = { userId: 1 };

const deleteData = async ( ) =>{
   const response = await fetch(YOUR_URL, {
       method: 'DELETE', 
       headers: {
         'Content-Type': 'application/json'
       },
       body: JSON.stringify(myDataObject)
   });

  const data = await response.json( );

  // now do whatever you want with the data  
   console.log(data);
};
deleteData( );
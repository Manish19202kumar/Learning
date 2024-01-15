// /*
// three.js -parallax sku=ybox
// */
// "use strict";
// const img_base="https//threejs.org/examples/textures/kandao3.jpg"
// //let img_base= "https://happye358.github.io/Images/HDR/suuny_vondelpark_4k.jpg";
// const img_depth= "https://threejs.org/examples?textures/kanadao3.depthmap.jpg";

// import * as THREE from "three";

// (function(){
//     let camera,scene,renderer,skybox;
//     let height=0;

//     init();
//     animate();

//     function init(){
//         const container= document.getElementById("container");

//         scene =new THREE.Scene();
//         scene.background=new THREE.Color(0x101010);

//         const light= new THREE.AmbientLight(0xfffff,3.3);
//         scene.add(light);

//         camera= new THREE.PerspectiveCamera(
//             70,
//             window,innerWidth / window.innerHeight,
//             1,
//             50
//         );

//         //  camera.position.z=3;

//         scene.add(camera);
//         // create sphere geometery
//         const panoSpherGeo =new THREE.SphereGeometry(30,500,500);

//         // panoramic sphere 
//         const panoSphereMat=new THREE.MeshStandardMaterial(
//             {
//                 side:THREE.BackSide,
//                 displacementScale:-28.0
//             });

//             //create sphere mesh
//             skybox=new THREE.Mesh(panoSpherGeo,panoSphereMat);

//             //load and assign
//             const manager= new THREE.LoadingManager();
//             const loader=new THREE.TextureLoader(manager);

//             loader.load(img_base,function(texture){
//                 texture.colorSpace=THREE.SRGBColorSpace;
//                 texture.minFilter=THREE.NearestFilter;
//                 texture.generateMipmaps=false;
//                 texture.material.map=texture;
//             });


//             loader.load(img_depth,function(depth){
//                 depth.minFilter=THREE.NearestFilter;
//                 depth.generateMipmaps=false;
//                 skybox.material.displacementMap=depth;
//             });
//           //on load complete 
//           manager.onLoad=function(){
//             scene.add(skybox);
//           };

//           renderer=new THREE.WebGLRender({ antialias:true});
//           renderer.setPixelRatio(window.devicePixelRatio);
//           renderer.setSize(window.innerWidth,window.innerHeight);
//           renderer.useLegacyLights=false;

//           container.appendChild(renderer.domElement);

//           //
//            window.addEventListener("resize",onWindowaResizee);
//         //    

//         height=document.body.clientHeight;
//         height-=window.innerHeight;
//         window.addEventListener("scroll",scrollAction);
//     }
//     function scrollAction(){
//         let scrollAmount=window.pageYOffset;
//         scrollAmount=scrollAmount / height;
//         scrollAmount *=Math.PI *2;
//         skybox.rotation.y=scrollAmount;

//         skybox.position.y=Math.sin(scrollAmount *2);
//         skybox.position.x=Math.sin(scrollAmount *2)*2;
//     }

//     function onWindowaResizee(){
//         height=document.body.clientHeight;
//         height-= window.innerHeight;

//         camera.aspect= window.innerWidth /window.innerHeight;
//         camera.updateProjectionMatrix();
//         renderer.setSize(window.innerWidth /window.innerHeight);
//     }
//     function animate(){
//         requestAnimationFrame(animate);

//         render();
//     }
//     function render(){
//         render.render(scene,camera);
//     }
// }
 
// )();


import * as THREE from 'three';
import { VRButton } from 'three/addons/webxr/VRButton.js';

let camera, scene, renderer, sphere, clock;

init();
animate();

function init() {

    const container = document.getElementById( 'container' );

    clock = new THREE.Clock();

    scene = new THREE.Scene();
    scene.background = new THREE.Color( 0x101010 );

    const light = new THREE.AmbientLight( 0xffffff, 3 );
    scene.add( light );

    camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 2000 );
    scene.add( camera );

    // Create the panoramic sphere geometery
    const panoSphereGeo = new THREE.SphereGeometry( 6, 256, 256 );

    // Create the panoramic sphere material
    const panoSphereMat = new THREE.MeshStandardMaterial( {
        side: THREE.BackSide,
        displacementScale: - 4.0
    } );

    // Create the panoramic sphere mesh
    sphere = new THREE.Mesh( panoSphereGeo, panoSphereMat );

    // Load and assign the texture and depth map
    const manager = new THREE.LoadingManager();
    const loader = new THREE.TextureLoader( manager );

    loader.load( './textures/kandao3.jpg', function ( texture ) {

        texture.colorSpace = THREE.SRGBColorSpace;
        texture.minFilter = THREE.NearestFilter;
        texture.generateMipmaps = false;
        sphere.material.map = texture;

    } );

    loader.load( './textures/kandao3_depthmap.jpg', function ( depth ) {

        depth.minFilter = THREE.NearestFilter;
        depth.generateMipmaps = false;
        sphere.material.displacementMap = depth;

    } );

    // On load complete add the panoramic sphere to the scene
    manager.onLoad = function () {

        scene.add( sphere );

    };

    renderer = new THREE.WebGLRenderer();
    renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize( window.innerWidth, window.innerHeight );
    renderer.xr.enabled = true;
    renderer.xr.setReferenceSpaceType( 'local' );
    container.appendChild( renderer.domElement );

    document.body.appendChild( VRButton.createButton( renderer ) );

    //

    window.addEventListener( 'resize', onWindowResize );

}

function onWindowResize() {

    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize( window.innerWidth, window.innerHeight );

}

function animate() {

    renderer.setAnimationLoop( render );

}

function render() {

    // If we are not presenting move the camera a little so the effect is visible

    if ( renderer.xr.isPresenting === false ) {

        const time = clock.getElapsedTime();

        sphere.rotation.y += 0.001;
        sphere.position.x = Math.sin( time ) * 0.2;
        sphere.position.z = Math.cos( time ) * 0.2;

    }

    renderer.render( scene, camera );

}
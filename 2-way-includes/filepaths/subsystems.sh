# audio
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos cocos aud /audio
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot aud /servers/audio,/scene/audio
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de aud /AudioSystem,/AudioEngineWwise,/Microphone
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal aud /AudioLink,/AudioMixer,/AudioAnalyzer,/AudioMixerCore,/AudioExtensions,/AudioCaptureCore,/AudioCodecEngine,/AudioPlatformConfiguration,/AudioCaptureImplementations,/BinkAudioDecoder,/NonRealtimeAudioRenderer,/BinkAudioDecoder,/NonRealtimeAudioRenderer,/AVEncoder,/SoundFieldRendering,/SignalProcessing

# core
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos cocos cor /base,/math
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot cor /core,/scene/main
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de cor /LmbrCentral,/GraphCanvas,/GraphModel,/FastNoise,/GradientSignal,/SaveData,/SceneLoggingExample,/AWSClientAuth,/AWSCore,/AWSGameLift,/AWSMetrics
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal cor /ApplicationCore,/Core,/CoreOnline,/CoreUObject,/RHICore,/ImageCore,/InputCore,/SlateCore,/RenderCore,/PhysicsCore,/GeometryCore,/AnimationCore,/AudioMixerCore,/ApplicationCore,/CrashReportCore,/AudioCaptureCore,/LiveLinkAnimationCore,/Json,/JsonUtilities,/StreamingFile,/StreamingPauseRendering,/NetworkReplayStreaming,/StorageServerClient,/IESFile,/PakFile,/SandboxFile,/Serialization,/Cbor,/IPC,/XmlParser,/TimeManagement,/UELibrary,/Projects,/PropertyPath,/RigVM,/RSA

# editor
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos cocos edi /editor-support/cocostudio
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot edi /editor
# no editor for o3de
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal edi /BlueprintRuntime,/InteractiveToolsFramework,/Landscape,/Toolbox

# physics
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos cocos phy /physics,/physics3d
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot phy /servers/physics,/servers/physics_2d
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de phy /NvCloth,/PhysX,/PhysXDebug
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal phy /ClothingSystemRuntimeNv,/ClothingSystemRuntimeCommon,/ClothingSystemRuntimeInterface,/Foliage,/PhysicsCore,/PhysXCooking

# low level renderer
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos cocos llr /renderer
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot llr /servers/visual
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de llr /Atom,/AtomContent,/AtomLyIntegration,/AtomTressFX,/Camera,/CameraFramework,/StartingPointCamera,/VideoPlaybackFramework
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal llr /CinematicCamera,/GeometryCore,/GeometryFramework,/MaterialShaderQualitySettings,/MaterialShaderQualitySettings,/Renderer,/RenderCore,/SlateRHIRenderer,/SlateNullRenderer,/SoundFieldRendering,/StreamingPauseRendering,/NonRealtimeAudioRenderer,/TextureUtilitiesCommon,/RHI,/RHICore,/D3D12RHI,/SlateRHIRenderer,/VulkanRHI,/HeadMountedDisplay,/NullDrv

# online multiplayer
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos cocos omp /network
# godot has OMP mixed in COR
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de omp /Multiplayer,/MultiplayerCompression,/CertificateManager,/HttpRequestor,/Metastream,/Presence,/Twitch
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal omp /Net,/Networking,/NetworkFile,/NetworkFileSystem,/NetworkReplayStreaming,/MovieSceneTracks,/MeshConversionEngineTypes,/FriendsAndChat,/Online,/OodleDataCompression,/PacketHandlers,/Sockets,/ExternalRPCRegistry

# platform independence layer
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos cocos pla /platform
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot pla /platform
# o3de has PLA mixed with each subsystem
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal pla /Android,/Apple,/IOS,/Linux,/Unix,/Windows,/WebBrowser,/WebBrowserTexture,/PlatformThirdPartyHelpers

# resources
# cocos has RES mixed into COR and other subsystems
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot res /scene/resources
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de res /AssetValidation,/CustomAssetExample,/DevTextures,/Prefab,/PrimitiveAssets,/SceneProcessing,/TestAssetBuilder,/TextureAtlas
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal res /AssetRegistry,/ImageCore,/ImageWrapper,/ImageWriteQueue,/Media,/MediaUtils,/MediaAssets,/GameplayMediaEncoder,/CrunchCompression,/Datasmith,/RuntimeAssetCache

# gameplay foundations
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos cocos gmp /scripting
# godot has GMP mixed with COR
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de gmp /Achievements,/GameState,/GameStateSamples,/TickBusOrderViewer,/EditorPythonBindings,/ExpressionEvaluation,/PythonAssetBuilder,/ScriptAutomation,/ScriptCanvas,/ScriptCanvasDeveloper,/ScriptCanvasPhysics,/ScriptCanvasTesting,/ScriptedEntityTweener,/ScriptEvents
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal gmp /GameplayTags,/GameplayTasks,/GameplayMediaEncoder,/Messaging,/MessagingRpc,/MessagingCommon,/SessionMessages,/SessionServices,/TypedElementFramework,/TypedElementRuntime

# human interface devices
# cocos has hid mixed with COR
# godot has hid mixed with COR
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de hid /Gestures,/LocalUser,/StartingPointInput,/StartingPointMovement,/VirtualGamepad
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal hid /InputCore,/InputDevice,/EyeTracker

# debug
# cocos has it mixed in all subystems
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot deb /scene/debugger
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de deb /DebugDraw,/CrashReporting,/ImGui,/Profiler
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal deb /DeveloperSettings,/CrashReportCore,/PerfCounters,/SynthBenchmark,/TraceLog

# front end
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos cocos fes /ui
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot fes /scene/gui
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de fes /WhiteBox,/LyShine,/LyShineExamples,/MessagePopup,/UiBasics
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal fes /ColorManagement,/GameMenuBuilder,/MovieScene,/MoviePlayer,/MoviePlayerProxy,/MovieSceneTracks,/MovieSceneCapture,/Slate,/SlateCore,/SlateRHIRenderer,/SlateNullRenderer,/AVIWriter,/AppFramework,/AdvancedWidgets,/CEF3Utils,/WidgetCarousel,/UMG,/Overlay,/PreLoadScreen

# SDK
# cocos: no sdk on runtime folder
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot sdk /thirdparty
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de sdk /InAppPurchases
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal sdk /VulkanRHI,/CUDA,/D3D12RHI,/NVidia,/OpenGLDrv

# scene graph optimization
# cocos: not found
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot sgc /scene/3d
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de sgc /SceneProcessing
# unreal: not found

# skeletal animation
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos cocos ska /editor-support/spine
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot ska /scene/animation
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de ska /EMotionFX,/Maestro
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source /media/ullmann/HDDGabriel/engines/UnrealEngine/Engine/Source unreal ska /AnimationCore,/AnimGraphRuntime,/SkeletalMeshDescription,/MeshConversion,/MeshDescription,/MeshUtilitiesCommon,/MeshConversionEngineTypes,/MRMesh,/Navmesh,/RawMesh,/StaticMeshDescription,/SkeletalMeshDescription,/RawMesh,/LiveLinkInterface,/LiveLinkAnimationCore,/LiveLinkMessageBusFramework,/StaticMeshDescription,/LevelSequence,/MRMesh

# visual fx
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos /media/ullmann/HDDGabriel/engines/cocos2d-x/cocos cocos vfx /2d,/3d
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/godot /media/ullmann/HDDGabriel/engines/godot godot vfx /scene/2d
sh cpp-walker.sh /media/ullmann/HDDGabriel/engines/o3de /media/ullmann/HDDGabriel/engines/o3de o3de vfx /LyShine,/AtomLyIntegration
# unreal: not found
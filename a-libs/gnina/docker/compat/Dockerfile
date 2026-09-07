# Maximum Compatibility Build 

FROM nvidia/cuda:12.3.2-cudnn9-devel-ubuntu20.04

# get packages 
WORKDIR /root
ARG DEBIAN_FRONTEND="noninteractive"
RUN apt-get update -y
RUN apt-get install -y build-essential  libboost-all-dev libeigen3-dev libgoogle-glog-dev libprotobuf-dev protobuf-compiler libhdf5-dev libatlas-base-dev python3-dev librdkit-dev python3-numpy python3-pip python3-pytest swig 
RUN apt update ; apt upgrade -y ; apt-get -y install build-essential git wget libboost-all-dev libeigen3-dev libgoogle-glog-dev libprotobuf-dev protobuf-compiler libhdf5-dev libatlas-base-dev python3-dev librdkit-dev python3-numpy python3-pip python3-pytest libjsoncpp-dev python3-yaml libopenblas-dev liblapack-dev libgfortran-9-dev
RUN apt-get update -y && apt-get install git-all -y curl && apt-get update -y
RUN apt-get install -y cuda-toolkit-12-0
RUN apt-get install -y --allow-change-held-packages libcudnn9-cuda-12 libcudnn9-dev-cuda-12 libcudnn9-static-cuda-12
RUN pip3 install cmake==3.31.6 scikit-image pyquaternion google-api-python-client six ninja 
RUN pip3 install torch torchvision torchaudio mkl-static mkl-include

#select version of cuda here
RUN rm /usr/local/cuda && ln -s /usr/local/cuda-12.0 /usr/local/cuda

RUN git clone https://github.com/dkoes/openbabel.git && cd openbabel && mkdir build && cd build && cmake  -DBUILD_SHARED=OFF -DWITH_MAEPARSER=OFF -DWITH_COORDGEN=OFF -DPYTHON_BINDINGS=OFF -DRUN_SWIG=OFF .. && make -j4 && make install

RUN git clone https://github.com/intel/mkl-dnn.git && cd mkl-dnn && git checkout v3.5.3 && mkdir build && cd build && cmake ..  -DDNNL_LIBRARY_TYPE=STATIC && make -j4 && make install

# with pytorch 2.7 build of nccl fails - expect to be pip installed  -DUSE_SYSTEM_NCCL=1 ?
ENV TORCH_CUDA_ARCH_LIST="6.0;7.0;7.5;8.0;8.6;9.0"
RUN git clone https://github.com/pytorch/pytorch.git && cd pytorch && git checkout v2.4.1 && git submodule sync && git submodule update --init --recursive  && mkdir build && cd build && cmake .. -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda -DCMAKE_CUDA_ARCHITECTURES="60;61;70;75;80;90" -DUSE_STATIC_MKL=ON -DUSE_MKLDNN=ON -DBLAS=OpenBLAS -DBUILD_SHARED_LIBS=OFF -DBUILD_PYTHON=OFF  -DUSE_TENSORPIPE=OFF -DUSE_STATIC_NCCL=ON -DUSE_MPI=OFF -DTORCH_CUDA_ARCH_LIST="${TORCH_CUDA_ARCH_LIST}" && make -j4 && make install

RUN  cd pytorch/build && cmake .. -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda -DCMAKE_CUDA_ARCHITECTURES="60;61;70;75;80;90" -DUSE_STATIC_MKL=ON -DUSE_MKLDNN=ON -DBLAS=OpenBLAS -DBUILD_SHARED_LIBS=ON -DBUILD_PYTHON=OFF -DUSE_TENSORPIPE=OFF -DUSE_STATIC_NCCL=ON  -DUSE_MPI=OFF -DTORCH_CUDA_ARCH_LIST="${TORCH_CUDA_ARCH_LIST}" && make -j4 && make install

RUN cd openbabel/build && rm CMakeCache.txt && cmake  -DBUILD_SHARED=ON -DWITH_MAEPARSER=OFF -DWITH_COORDGEN=OFF -DPYTHON_BINDINGS=OFF -DRUN_SWIG=OFF .. && make -j4 && make install

RUN git clone https://github.com/gnina/libmolgrid.git && cd libmolgrid && mkdir build && cd build && cmake ..  && make -j4 && make install
 
ADD "https://github.com/gnina/gnina/commits?per_page=1" latest_commit

RUN git clone https://github.com/gnina/gnina.git; \
    cd gnina; mkdir build; cd build; \
    cmake -DCMAKE_CUDA_ARCHITECTURES=all .. ;\
    make -j4 ; make install 

    
#make "somewhat static" executable
#TODO: make this a cmake target
RUN cd gnina/build/gninasrc; \
/usr/bin/c++  -Wno-deprecated-declarations -Wno-unknown-pragmas -D_GLIBCXX_USE_CXX11_ABI=1 -O3 -DNDEBUG -Wl,--disable-new-dtags CMakeFiles/gnina.dir/main/main.cpp.o CMakeFiles/gninalibobj.dir/version.cpp.o CMakeFiles/gninalibobj.dir/lib/atom_constants.cpp.o CMakeFiles/gninalibobj.dir/lib/bfgs.cu.o CMakeFiles/gninalibobj.dir/lib/box.cpp.o CMakeFiles/gninalibobj.dir/lib/builtinscoring.cpp.o CMakeFiles/gninalibobj.dir/lib/cache.cpp.o CMakeFiles/gninalibobj.dir/lib/cache_gpu.cpp.o CMakeFiles/gninalibobj.dir/lib/cnn_torch_scorer.cpp.o CMakeFiles/gninalibobj.dir/lib/coords.cpp.o CMakeFiles/gninalibobj.dir/lib/covinfo.cpp.o CMakeFiles/gninalibobj.dir/lib/custom_terms.cpp.o CMakeFiles/gninalibobj.dir/lib/dl_scorer.cpp.o CMakeFiles/gninalibobj.dir/lib/device_buffer.cpp.o CMakeFiles/gninalibobj.dir/lib/everything.cpp.o CMakeFiles/gninalibobj.dir/lib/flexinfo.cpp.o CMakeFiles/gninalibobj.dir/lib/GninaConverter.cpp.o CMakeFiles/gninalibobj.dir/lib/grid.cpp.o CMakeFiles/gninalibobj.dir/lib/grid_gpu.cu.o CMakeFiles/gninalibobj.dir/lib/model.cpp.o CMakeFiles/gninalibobj.dir/lib/molgetter.cpp.o CMakeFiles/gninalibobj.dir/lib/monte_carlo.cpp.o CMakeFiles/gninalibobj.dir/lib/mutate.cpp.o CMakeFiles/gninalibobj.dir/lib/my_pid.cpp.o CMakeFiles/gninalibobj.dir/lib/naive_non_cache.cpp.o CMakeFiles/gninalibobj.dir/lib/non_cache.cpp.o CMakeFiles/gninalibobj.dir/lib/non_cache_cnn.cpp.o CMakeFiles/gninalibobj.dir/lib/obmolopener.cpp.o CMakeFiles/gninalibobj.dir/lib/parallel_mc.cpp.o CMakeFiles/gninalibobj.dir/lib/parallel_progress.cpp.o CMakeFiles/gninalibobj.dir/lib/parse_pdbqt.cpp.o CMakeFiles/gninalibobj.dir/lib/pdb.cpp.o CMakeFiles/gninalibobj.dir/lib/PDBQTUtilities.cpp.o CMakeFiles/gninalibobj.dir/lib/quasi_newton.cpp.o CMakeFiles/gninalibobj.dir/lib/quaternion.cu.o CMakeFiles/gninalibobj.dir/lib/random.cpp.o CMakeFiles/gninalibobj.dir/lib/result_info.cpp.o CMakeFiles/gninalibobj.dir/lib/ssd.cpp.o CMakeFiles/gninalibobj.dir/lib/szv_grid.cpp.o CMakeFiles/gninalibobj.dir/lib/terms.cpp.o CMakeFiles/gninalibobj.dir/lib/weighted_terms.cpp.o CMakeFiles/gninalibobj.dir/lib/conf.cpp.o CMakeFiles/gninalibobj.dir/lib/conf_gpu.cu.o CMakeFiles/gninalibobj.dir/lib/gpucode.cu.o CMakeFiles/gninalibobj.dir/lib/model.cu.o CMakeFiles/gninalibobj.dir/lib/non_cache_gpu.cu.o CMakeFiles/gninalibobj.dir/lib/precalculate_gpu.cu.o CMakeFiles/gninalibobj.dir/lib/torch_model.cpp.o CMakeFiles/gninalibobj.dir/lib/tree_gpu.cu.o CMakeFiles/gninalibobj.dir/lib/user_opts.cpp.o CMakeFiles/gninalibobj.dir/torch_models.cpp.o CMakeFiles/gnina.dir/cmake_device_link.o -o ../bin/gnina.static   -L/usr/local/cuda/targets/x86_64-linux/lib/stubs  -L/usr/local/cuda/targets/x86_64-linux/lib  -Wl,-rpath,/usr/local/lib:/usr/local/cuda/lib64: all_default_to_default_1.3_1.o all_default_to_default_1.3_2.o all_default_to_default_1.3_3.o crossdock_default2018_1.3_1.o crossdock_default2018_1.3_2.o crossdock_default2018_1.3_3.o crossdock_default2018_1.3_4.o crossdock_default2018_1.3.o crossdock_default2018_1.o crossdock_default2018_2.o crossdock_default2018_3.o crossdock_default2018_4.o crossdock_default2018_KD_1.o crossdock_default2018_KD_2.o crossdock_default2018_KD_3.o crossdock_default2018_KD_4.o crossdock_default2018_KD_5.o crossdock_default2018.o default2017.o dense_1.3_1.o dense_1.3_2.o dense_1.3_3.o dense_1.3_4.o dense_1.3.o dense_1.3_PT_KD_1.o dense_1.3_PT_KD_2.o dense_1.3_PT_KD_3.o dense_1.3_PT_KD_4.o dense_1.3_PT_KD_def2018_1.o dense_1.3_PT_KD_def2018_2.o dense_1.3_PT_KD_def2018_3.o dense_1.3_PT_KD_def2018_4.o dense_1.3_PT_KD_def2018.o dense_1.3_PT_KD.o dense_1.o dense_2.o dense_3.o dense_4.o dense.o general_default2018_1.o general_default2018_2.o general_default2018_3.o general_default2018_4.o general_default2018_KD_1.o general_default2018_KD_2.o general_default2018_KD_3.o general_default2018_KD_4.o general_default2018_KD_5.o general_default2018.o redock_default2018_1.3_1.o redock_default2018_1.3_2.o redock_default2018_1.3_3.o redock_default2018_1.3_4.o redock_default2018_1.3.o redock_default2018_1.o redock_default2018_2.o redock_default2018_3.o redock_default2018_4.o redock_default2018_KD_1.o redock_default2018_KD_2.o redock_default2018_KD_3.o redock_default2018_KD_4.o redock_default2018_KD_5.o redock_default2018.o /usr/lib/x86_64-linux-gnu/libboost_program_options.a /usr/lib/x86_64-linux-gnu/libboost_system.a /usr/lib/x86_64-linux-gnu/libboost_iostreams.a /usr/lib/x86_64-linux-gnu/libboost_timer.a /usr/lib/x86_64-linux-gnu/libboost_thread.a /usr/lib/x86_64-linux-gnu/libboost_serialization.a /usr/lib/x86_64-linux-gnu/libboost_filesystem.a /usr/lib/x86_64-linux-gnu/libboost_date_time.a /usr/lib/x86_64-linux-gnu/libboost_regex.a /usr/lib/x86_64-linux-gnu/libboost_unit_test_framework.a /usr/local/lib/libopenbabel.a /usr/local/lib/libmolgrid.a -Wl,--whole-archive /usr/local/lib/libtorch.a -Wl,--no-whole-archive -Wl,--whole-archive /usr/local/lib/libtorch_cpu.a /usr/lib/gcc/x86_64-linux-gnu/9/libgomp.a  /usr/local/lib/libtorch_cuda.a -Wl,--no-whole-archive  -lcudnn -L/usr/local/cuda/lib64 -lcudart -lcusparse -lcufft -lnvToolsExt -lcurand -lcublas -lcublasLt  -lcusolver -Wl,--whole-archive  /root/pytorch/build/nccl/lib/libnccl_static.a /usr/local/lib/libc10_cuda.a -Wl,--no-whole-archive /usr/local/lib/libc10.a /usr/local/lib/libnnpack.a /lib/x86_64-linux-gnu/libnuma.a /usr/local/lib/libpytorch_qnnpack.a   /usr/local/lib/libXNNPACK.a /usr/local/lib/libprotobuf-lite.a /usr/local/lib/libprotobuf.a /usr/local/lib/libprotoc.a /usr/local/lib/libfmt.a /usr/local/lib/libcpuinfo.a /usr/local/lib/libclog.a /usr/local/lib/libpthreadpool.a  /usr/local/lib/libfbgemm.a /usr/local/lib/libdnnl.a /usr/local/lib/libdnnl.a /usr/local/lib/libsleef.a /usr/local/lib/libasmjit.a /usr/local/lib/libkineto.a /usr/local/cuda/lib64/libcupti_static.a -lnvToolsExt -lcudart_static -ldl -lrt /usr/lib/x86_64-linux-gnu/libz.a /usr/lib/x86_64-linux-gnu/libboost_chrono.a /root/pytorch/build/lib/libgloo.a /root/pytorch/build/lib/libgloo_cuda.a /usr/lib/x86_64-linux-gnu/libboost_atomic.a /usr/lib/x86_64-linux-gnu/libjsoncpp.a /root/pytorch/build/lib/libonnx.a /root/pytorch/build/lib/libonnx_proto.a /usr/lib/x86_64-linux-gnu/libopenblas.a /usr/lib/gcc/x86_64-linux-gnu/9/libgfortran.a /usr/lib/gcc/x86_64-linux-gnu/9/libquadmath.a  -lcudadevrt -lcudart_static -pthread

#./bin/gnina -r ../test/gnina/data/184l_rec.pdb -l ../test/gnina/data/184l_lig.sdf --autobox_ligand ../test/gnina/data/184l_lig.sdf --seed 0



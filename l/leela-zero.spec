Name: leela-zero
Summary: Go engine with no human-provided knowledge, modeled after the AlphaGo Zero paper
Version: 0.17git
Release: 1
Group: games
License: GPLv3
URL: https://github.com/gcp/leela-zero
#Source0: %{name}-%{version}.tar.gz
Source0: %{name}-master.zip
BuildRequires: boost-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: openblas-devel
BuildRequires: ocl-icd-devel
BuildRequires: opencl-headers

%description
A Go program with no human provided knowledge. Using MCTS (but without Monte
Carlo playouts) and a deep residual convolutional neural network stack.

This is a fairly faithful reimplementation of the system described in the
Alpha Go Zero paper "Mastering the Game of Go without Human Knowledge". For
all intents and purposes, it is an open source AlphaGo Zero.
https://deepmind.com/documents/119/agz_unformatted_nature.pdf

No network weights are in this repository. If you manage to obtain the AlphaGo
Zero weights, this program will be about as strong, provided you also obtain a
few Tensor Processing Units. Lacking those TPUs, the author recommends a top
of the line GPU - it's not exactly the same, but the result would still be an
engine that is far stronger than the top humans.

Recomputing the AlphaGo Zero weights will take about 1700 years on commodity
hardware. Upstream is running a public, distributed effort to repeat this
work. Working together, and especially when starting on a smaller scale, it
will take less than 1700 years to get a good network (which you can feed into
this program, suddenly making it strong). To help with this effort, run the
leelaz-autogtp binary provided in this package. The best-known network weights
file is at https://zero.sjeng.org/best-network

%prep
%setup -q -n %{name}-master
#sed -i '26i #include <string>' src/TimeControl.h

%build
%cmake -DOpenCL_LIBRARY=/usr/lib64/libOpenCL.so
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS COPYING *.md
%{_bindir}/*

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.17git
- Rebuilt for Fedora

Name: mclinker
Summary: LLVM Linker for Mobile Computing
Version: 2.5.0
Release: 1
Group: Development/Tools
License: BSD-Style
URL: https://code.google.com/p/mclinker/
Source0: https://mclinker.googlecode.com/files/%{name}-Momo.tar.bz2
BuildRequires: llvm-devel
BuildRequires: bison

%description
MCLinker is a full-fledged system linker for mobile devices. It supports
multiple platforms (ARM, X86 and Mips). It is fast, small with low memory
footprints. And the best, MCLinker is UIUC BSD-Style open source.

%prep
%setup -q -n %{name}-Momo

%build
%configure
make

%install
make install DESTDIR=%{buildroot}

%files
%doc ChangeLog README COPYING TODO

%changelog
* Sun Aug 24 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.0
- Rebuilt for Fedora

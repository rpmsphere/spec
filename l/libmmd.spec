%undefine _debugsource_packages

Summary: A library for rendering mikumiku files
Name: libmmd
Version: 0.7.2
Release: 7.1
License: GPL
Group: System/Library
Source0: https://frostworx.de/files/%{name}-%{version}.tar.gz
URL: https://www.frostworx.de/?p=43
BuildRequires: gcc-c++, bullet-devel, mesa-libGL-devel, mesa-libGLU-devel

%description
A library for a rendering mikumiku dance pmd model and vmd motion files.
The original sourcecode is part of the windows program MMD_Desktop (v0.4.9): https://r13n.spaces.live.com
which in turn took its sources from ARTK_MMD (v0.7), which can be found under https://ppyy.hp.infoseek.co.jp/artk_mmd.html
Both MMD_Desktop and artk-mmd are released under the GPL-2 license, so I assume that putting this lib under GPL-2 too is ok.
The code in this archive is almost unmodified, just some linux changes and switch to a shared library (changes are included as a diff).
I changed the code to a shared lib, as there are several other opensource programs which (could) make use of the code.

%package devel
Summary: libmmd Header files and documents.
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}

%description devel
libmmd C develop header files.
You can learn how to use api by documents and examples.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%__mkdir_p $RPM_BUILD_ROOT%{_libdir}
%__mkdir_p $RPM_BUILD_ROOT%{_includedir}/mmd
%__cp -a *.so* $RPM_BUILD_ROOT%{_libdir}
%__cp -a *.h $RPM_BUILD_ROOT%{_includedir}/mmd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README
%{_libdir}/*.so*

%files devel
%{_includedir}/mmd/*

%changelog
* Mon May 23 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.2
- Rebuilt for Fedora

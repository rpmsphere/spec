%undefine _debugsource_packages

Name: fractalnow
Summary: Fast, advanced fractal generator
Version: 0.8.2
Release: 4.1
Group: Science
License: LGPLv3
URL: https://fractalnow.sourceforge.net
Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires: desktop-file-utils
BuildRequires: qt5-qtbase-devel
BuildRequires: libmpc-devel
BuildRequires: mpfr-devel

%description
FractalNow provides users with tools to generate pictures of various types of
fractals quickly and easily.

It is made of both a command line (FractalNow) and a graphical tool
(QFractalNow).

The graphical tool, based on Qt library, allows users to explore fractals
intuitively and generate pictures.

Both tools are entirely multi-threaded and implement advanced algorithms and
heuristics that make computation very fast compared to most existing free
fractal generators.

%prep
%setup -q
sed -i 's|qmake|qmake-qt5|' configure

%build
./configure -prefix /usr
sed -i 's|-O2|-O2 -fPIC|' lib/Makefile
make %{?_smp_mflags}

%install
make install PREFIX=%{buildroot}/usr
sed -i 's|Qt;Education;Science;Math;|Graphics;|' %{buildroot}%{_datadir}/applications/q%{name}.desktop

%files
%{_bindir}/*
%{_datadir}/applications/q%{name}.desktop
%{_datadir}/doc/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/q%{name}.png
%{_datadir}/pixmaps/*

%changelog
* Mon Sep 10 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.2
- Rebuilt for Fedora

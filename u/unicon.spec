%undefine _debugsource_packages

Summary:	The Unified Extended Dialect of Icon
Name:		unicon
Version:	13.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	https://sourceforge.net/projects/unicon/files/%{name}_%{version}.tar.gz
URL:		https://unicon.sourceforge.net/
BuildRequires:	libX11-devel libXft-devel
BuildRequires:  mesa-libGL-devel libjpeg-turbo-devel libvorbis-devel

%description
Unicon is a very high level object-oriented network-savvy, graphics-savvy
programming language with a syntax similar to Pascal or C. Novel control and
data structures make Unicon ideal for rapidly solving complex problems.

%prep
%setup -q -n %{name}

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
%ifarch x86_64
make name=x86_64_linux
%else
%ifarch aarch64
make name=arm_64_linux
%else
make name=x86_32_linux
%endif
%endif
make Unicon

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_docdir}/%{name}
%{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Fri Mar 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 13.2
- Rebuilt for Fedora

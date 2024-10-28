%global __spec_install_post %{nil}
%undefine _debugsource_packages

Name:          ladcca
Version:       0.4.0
Release:       11.1
Summary:       A session management system for JACK and ALSA audio applications
Group:         System/Multimedia
URL:           https://lash-audio-session-handler.org/
Source:        https://lash-audio-session-handler.org/download/%{name}-%{version}.tar.gz
Patch0:        %{name}-0.4.0-deprecated_jackAPI.patch
License:       GPL
BuildRequires: alsa-lib-devel
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: e2fsprogs-devel
BuildRequires: expat-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: glib-devel
#BuildRequires: glitz-devel
BuildRequires: gtk+-devel
BuildRequires: gtk2-devel
BuildRequires: pipewire-jack-audio-connection-kit-devel
BuildRequires: ncurses-devel
BuildRequires: pango-devel
BuildRequires: pixman-devel
BuildRequires: libpng-devel
BuildRequires: readline-devel
BuildRequires: libselinux-devel
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: libxcb-devel
BuildRequires: xcb-util-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXext-devel
BuildRequires: libxml2-devel
BuildRequires: libXrender-devel
BuildRequires: zlib-devel
BuildRequires: libuuid-devel
Requires:      libladcca-devel == %{version}

%description
LASH is a session management system for JACK and ALSA audio applications
on GNU/Linux. It is an implementation of this proposal that originated
from this discussion. Its aim is to allow you to have many different
audio programs running at once, to save their setup, close them down
and then reload the setup at some other time. LASH doesn't deal with
any kind of audio data itself; it just runs programs, deals with
saving/loading (arbitrary) data and connects different kinds of virtual
audio ports together (currently JACK and ALSA sequencer ports.)

%package -n libladcca
Summary:       Devel package for %{name}
Group:         System/Libraries

%description -n libladcca
LASH is a session management system for JACK and ALSA audio applications on GNU/Linux. It is an implementation of this proposal that originated from this discussion. Its aim is to allow you to have many different audio programs running at once, to save their setup, close them down and then reload the setup at some other time. LASH doesn't deal with any kind of audio data itself; it just runs programs, deals with saving/loading (arbitrary) data and connects different kinds of virtual audio ports together (currently JACK and ALSA sequencer ports.)

%package -n libladcca-devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      libladcca = %{version}

%description -n libladcca-devel
LASH is a session management system for JACK and ALSA audio applications on GNU/Linux. It is an implementation of this proposal that originated from this discussion. Its aim is to allow you to have many different audio programs running at once, to save their setup, close them down and then reload the setup at some other time. LASH doesn't deal with any kind of audio data itself; it just runs programs, deals with saving/loading (arbitrary) data and connects different kinds of virtual audio ports together (currently JACK and ALSA sequencer ports.)

This package contains static libraries and header files need for development.

%prep
%setup -q 
%patch 0 -p1
sed -i 's|-number|-number-sections|' docs/Makefile*

%build
export LDFLAGS=-lm
%configure \
   --disable-serv-inst \
   --disable-gtk \
   --disable-gtktest \
   --disable-texi2html
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files 
%{_bindir}/*
%{_infodir}/ladcca-manual.info*
%exclude %{_infodir}/dir
%{_datadir}/ladcca/dtds/ladcca-project-1.0.dtd

%files -n libladcca
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README README.SECURITY TODO
%{_libdir}/*.so.*

%files -n libladcca-devel
%dir %{_includedir}/ladcca-1.0/ladcca
%{_includedir}/ladcca-1.0/ladcca/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libladcca.so
%{_libdir}/libladcca.a
%{_libdir}/libladcca.la

%changelog
* Sun Mar 19 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
* Sat Jun 13 2009 Automatic Build System <autodist@mambasoft.it> 0.4.0-3mamba
- automatic rebuild by autodist
* Mon Apr 07 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 0.4.0-2mamba
- specfile updates
* Sun Feb 20 2005 Silvan Calarco <silvan.calarco@mambasoft.it> 0.4.0-1qilnx
- package created by autospec

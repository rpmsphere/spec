%undefine _debugsource_packages
Summary:   FLTK version of TeacherTool
Name:      fl-teachertool
Version:   0.71
Release:   17.1
URL:       https://www3.telus.net/public/robark/Fl_TeacherTool/
Source0:   fl_teachertool-%{version}.tar.bz2
Source1:   fl_teachertool.desktop
Patch0:	   fl_teachertool-makefile.patch
Patch1:	   fl_teachertool.cxx.patch
Patch2:    fl_teachertool-iptables-path.patch
Patch3:	   fl_teachertool-more-fixes.patch
License:   GPL
Group:     User Interface/Desktops
BuildRequires: fltk-devel gcc-c++ libXpm-devel xorg-x11-proto-devel libX11-devel libpng-devel libjpeg-devel freetype-devel
BuildRequires: python2
Requires:  tightvnc vncsnapshot vnc-reflector

%description
FLTK version of TeacherTool.

%prep
%setup -q -n fl_teachertool-%{version}
%patch0
%patch1 -p1
%patch2 -p1

%build
export SUSE_ASNEEDED=0
%__make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/applications/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/usr/share/applications/
%makeinstall

%post
%__cp /usr/bin/vncviewer /usr/bin/teachertool-vncviewer
%__cp /usr/bin/vncpasswd /usr/bin/teachertool-vncpasswd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING INSTALL RELEASE-NOTES
%config /etc/fl_teachertool/HOST_INFO_FILE
%config /etc/fl_teachertool/fl_teachertool.conf
%dir /etc/fl_teachertool
/etc/fl_teachertool/*.jpg
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/applications/fl_teachertool.desktop

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.71
- Rebuilt for Fedora
* Tue Nov 10 2009 cyberorg@opensuse.org
- Update to 0.71
- Now works with LTSP5
* Sun Aug 31 2008 cyberorg@opensuse.org
- Update to 0.62

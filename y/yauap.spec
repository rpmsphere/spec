Name:          yauap
Version:       0.2.4
Release:       2.1
Summary:       The useless audio player
Group:         Applications/Multimedia
URL:           http://www.nongnu.org/yauap/
Source:        http://download.savannah.gnu.org/releases/yauap/yauap-%{version}.tar.gz
License:       LGPL
Requires:      gstreamer-plugins-base
BuildRequires: gstreamer-plugins-base
BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: gstreamer-plugins-base-devel
BuildRequires: gstreamer-devel
BuildRequires: libxml2-devel

%description
yauap is a simple commandline audio player based on GStreamer.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/yauap
%doc COPYING ChangeLog README

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.4
- Rebuilt for Fedora
* Sun Mar 22 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.2.4-1mamba
- automatic update by autodist
* Sun Jan 11 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.2.3-1mamba
- automatic update by autodist
* Tue Aug 19 2008 gil <puntogil@libero.it> 0.2.2-1mamba
- package created by autospec

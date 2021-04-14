Name:           hamachi-gui
Version:        0.9.6
Release:        7.1
Summary:        GUI for the Zero Configuration VPN Client Hamachi
Source:         http://prdownloads.sourceforge.net/hamachi-gui/hamachi-gui_%{version}.tar.gz
# PATCH-FIX-UPSTREAM hamachi-gui-fix-includes.patch -- Repairs common error: lack of "#include <string.h>"
Patch0:         hamachi-gui-fix-includes.patch
# PATCH-FIX-UPSTREAM hamachi-gui-0.9.6-abuild.patch adam@mizerski.pl -- Fixes linking. Here is why it failed before: https://bugzilla.novell.com/show_bug.cgi?id=533563
Patch1:         hamachi-gui-0.9.6-abuild.patch
URL:            http://hamachi-gui.sourceforge.net/
Group:          Productivity/Networking/Security
License:        GNU General Public License version 2(GPL v2)
BuildRequires:  glib2-devel gtk2-devel libxml2-devel libglade2-devel
BuildRequires:  gcc make glibc-devel pkgconfig intltool gettext gettext-devel
BuildRequires:  autoconf automake libtool desktop-file-utils

%description
hamachi-gui is a graphical user interface (GUI) for the zero configuration
VPN client Hamachi. The official client for Linux has only a command line
interface. hamachi-gui provides a user friendly GUI with comparable features
and more.

Authors:
--------
    Viktor Nordell <viktor.nordell@gmail.com>

%prep
%setup -q
%patch0
%patch1 -p1

%build
CFLAGS="%{optflags} -g -lX11" CXXFLAGS="%{optflags} -g -lX11" \
%configure
%__make %{?jobs:-j%{jobs}}

%install
%__rm -rf "$RPM_BUILD_ROOT"
%makeinstall
%__mv "$RPM_BUILD_ROOT%{_datadir}/locale"/{no,nb_NO}
%find_lang "%{name}"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files -f "%{name}.lang"
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/hamachi-gui
%{_datadir}/applications/hamachi-gui.desktop
%{_datadir}/hamachi-gui

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.6
- Rebuilt for Fedora
* Mon Mar  8 2010 Adam Mizerski <adam@mizerski.pl> 0.9.6
- fixed mistake in hamachi-gui.spec about applying abuild patch
* Sun Mar  7 2010 Adam Mizerski <adam@mizerski.pl> 0.9.6
- added hamachi-gui-0.9.6-abuild.patch
* Sat May  2 2009 Pascal Bleser <pascal.bleser@opensuse.org> 0.9.6
- update to 0.9.6:
  * translation updates
* Sat Mar  8 2008 Pascal Bleser <guru@unixtech.be> 0.9.5
- new package

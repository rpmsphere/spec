Name:				 u3-tool
Version:			 0.3
Release:			 2.1
Summary:			 U3 Smart Drive USB Flash Disk Control Tool
# http://prdownloads.sourceforge.net/u3_tool/u3-tool-%{version}.tar.gz
Source:			 u3-tool-%{version}.tar.bz2
URL:				 http://u3-tool.sourceforge.net/
Group:			 Hardware/Other
License:			 GNU General Public License version 2 or later (GPL v2 or later)
BuildRoot:		 %{_tmppath}/build-%{name}-%{version}
BuildRequires:	 gcc make glibc-devel
BuildRequires:	 autoconf automake libtool

%description
Tool for controlling USB flash devices that confirm to the U3 specifications.

This program can control the following features:
* Replacing of CD image
* Changing of virtual CD allocated size and completely removing it
* Enabling and disabling Security
* Unlocking and changing password of secured U3 device
* Obtainig various device information

Authors:
--------
    daviedev <daviedev@users.sourceforge.net>

%prep
%setup -q

%build
%configure
%__make %{?jobs:-j%{jobs}}

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install

h=/usr/share/doc/licenses/md5/$(md5sum COPYING|cut -f1 -d" ")
test -e "$h" && %__ln_s -f "$h" .

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_sbindir}/u3-tool
%doc %{_mandir}/man1/u3-tool.1.*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora

* Sat Feb 13 2010 pascal.bleser@opensuse.org
- initial build (0.3)

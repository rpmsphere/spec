%global debug_package %{nil}

Name:		evilwm
Version:	1.1.1
Release:	7.1
URL:		http://evilwm.sourceforge.net/
Source0:	http://www.6809.org.uk/evilwm/%{name}-%{version}.tar.gz
License:	Public Domain
Group:		Graphical desktop/Other
Summary:	A minimalist window manager for the X Window System
BuildRequires:	nas-devel 
BuildRequires:	motif-devel 
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:	libXrandr-devel

%description
The name evil came from Stuart 'Stuii' Ford, who thinks that any software
I use must be evil and masochistic.  In reality, this window manager is
clean and easy to use.

FEATURES:
 * No window decorations apart from a simple 1 pixel border.
 * No icons.
 * Good keyboard control, including repositioning and maximise toggles.
 * Solid window drags (compile time option - may be slow on old machines).
 * Virtual desktops.
 * Small binary size (even with everything turned on).

%prep
%setup -q
perl -pi -e 's!^#DEFINES.*-DVDESK.*!DEFINES += -DVDESK!' Makefile

%build
make

%install
%makeinstall

%files
%doc README ChangeLog TODO
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Mar 10 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuild for Fedora

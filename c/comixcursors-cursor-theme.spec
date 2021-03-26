Name:           comixcursors-cursor-theme
License:        GPL
Group:          User Interface/Desktops
Summary:        The original Comix Cursors
Version:        0.9.0
Release:        2.1
Source0:        http://www.limitland.de/comixcursors/ComixCursors-%{version}.tar.bz2
URL:            http://gnome-look.org/content/show.php/ComixCursors?content=32627
BuildArch:      noarch

%description
ComixCursors is a set of mouse pointer themes for X11 in the style of comic-book art.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a ComixCursors-* $RPM_BUILD_ROOT%{_datadir}/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/ComixCursors-*

%changelog
* Sat Sep 24 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0
- Rebuild for Fedora

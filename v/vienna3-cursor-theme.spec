%define theme_name Vienna3

Summary:        Vienna3 cursor theme
Name:           vienna3-cursor-theme
Version:        20080614
Release:        2.1
License:        freeware
Group:          User Interface/Desktops
URL:            http://s0ury.deviantart.com/art/J-Aroche-s-Vienna3-Converted-88493695?q=1&qo=1
Source0:        http://www.deviantart.com/download/88493695/j_aroche__s_vienna3_converted_by_s0ury.zip
BuildArch:      noarch

%description
J. Aroche's Vienna3 for CursorXP, converted to an X11 cursor.
Javier has agreed on providing me a ubuntu logo animation for the 'AppStarting'
animation, previously has a Windows logo. Some animations have been changed to
ones that don't cause glitches on the desktop when compiz-fusion is enabled,
and the "hand" image has been replaced with a much more interesting animation
from J.Aroche. Link to Original for CursorXP:
http://www.wincustomize.com/skins.aspx?skinid=2412&libid=25

%prep
%setup -q -c
tar xf %{theme_name}.tar.gz

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a %{theme_name}/* $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/icons/%{theme_name}

%changelog
* Thu Dec 08 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20080614
- Rebuilt for Fedora

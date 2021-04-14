%define theme_name black-white-2
%define _theme_name black-white_2-Style

Name:		blackwhite2-icon-theme
Version:	2.0
Release:	3.1
Summary:	Black-White-2-Style icon theme
Group:		User Interface/Desktops
License:	GPL
URL:		http://dbgthekafu.deviantart.com/art/black-white-2-Style-73276755
Source0:	black_white_2_Style_by_DBGtheKafu.tar
BuildArch:	noarch

%description
New in this version is:
-Much smaller! “black-white 2” has only a size of 10 Mb, but has much more icons -More Icons!
-Folder Icons! In black-white 2 there are some new icons for your download, document, music, ...., folder.
-different title bar sizes! when u download “black-white 2” you can choose big or normal.
The “big” version has a little bit bigger action icons like in “black-white”.
-different main menu icons! in “black-white 2” you can choose between 12 start icons.

%prep
%setup -q -n black-white\ 2\ Style
tar -zxf %{_theme_name}.tar.gz -C .

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/icons
cp -a %{_theme_name} %{buildroot}%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora

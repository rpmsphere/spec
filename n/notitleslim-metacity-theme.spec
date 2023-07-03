%define theme_name NoTitleSlim

Name:           notitleslim-metacity-theme
Version:        1.0
Release:        3.1
Summary:        No-Title Slim metacity theme
Group:          User Interface/Desktops
License:        GPL
URL:            https://gnome-look.org/content/show.php/No-Title+Slim?content=123715
Source0:        NoTitleSlim.tar.gz
BuildArch:      noarch

%description
Based on No-Title theme by jeansch
https://gnome-look.org/content/show.php/No-Title?content=93438
Titlebars are not really useful! Especially on 1280x800 or less screens :)

This theme fits any GTK theme using its colors.
It is a bit thiner than No-Title and maximized windows have reduced decorations.
I left some decoration though cause on some GTK themes window could blend with
the top or the bottom panel. If you want to get rid of all decorations in
maximized state, you may change all non-zero numbers to zero in frame_geometry
"maximized" section.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Mon Aug 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora

%define theme_name Dalisha

Summary:        %{theme_name} icon theme
Name:           dalisha-icon-theme
Version:        2.99
Release:        2.1
License:        GPL2+
Group:          User Interface/Desktops
URL:            http://gnome-look.org/content/show.php/Dalisha?content=166286
Source0:        %{theme_name}_2_99.tar.gz
BuildArch:      noarch

%description
A simple icon set for Linux.
(this version without 256x256 icons)

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/icons/%{theme_name}

%changelog
* Fri Aug 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.99
- Rebuilt for Fedora

%define theme_name Meliae

Summary: %{theme_name} icon theme
Name: meliae-icon-theme
Version: 0.7
Release: 3.1
License: GPL
Group: User Interface/Desktops
URL: http://gnome-look.org/content/show.php/Meliae?content=88482
Source0: http://dl.dropboxusercontent.com/u/24716740/mirror/%{theme_name}.tar.gz
Source1: http://dl.dropboxusercontent.com/u/24716740/mirror/%{theme_name}White.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
Meliae Dark and White icon theme.

%prep
%setup -q -c -a 1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a %{theme_name}* $RPM_BUILD_ROOT%{_datadir}/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/icons/%{theme_name}*

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7
- Rebuild for Fedora

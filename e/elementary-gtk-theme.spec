%define theme_name elementary

Name:		%{theme_name}-gtk-theme
Version:	2.1
#Version:   3
Release:	11.1
Summary:	Elementary GTK theme
Group:		User Interface/Desktops
License:	GPLv2+
BuildArch:	noarch
URL:		http://danrabbit.deviantart.com/art/%{name}-83104033	
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}.gtkrc.patch
BuildRequires:  libpng-devel
BuildRequires:	gtk2-devel
Requires:	gtk-murrine-engine
Requires:	elementary-icon-theme
Requires:   dmz-cursor-themes

%description
This package contains the Elementary GTK Theme for the GNOME desktop.

%prep
%setup -q -n %{theme_name}-gtk-%{version}
%patch0
sed -i -e 's|%{theme_name} Dark|%{theme_name}|' -e 's|DMZ-Black|dmz-aa|' index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a AUTHORS CONTRIBUTORS COPYING index.theme metacity-1 gtk-2.0 $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Sun Jan 08 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuild for Fedora
* Mon Mar 14 2011 Chris Smart <chris@kororaa.org> 2.1-1
- Initial port from oxygen-gtk.spec.

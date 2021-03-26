Summary: A non-file manager
Name: nemodocs
Version: 0.2.4
Release: 11.4
License: LGPL 2.1
Group: Applications/File
URL: http://www.iola.dk/nemo/
BuildArch: noarch
Source: http://www.iola.dk/nemo/downloads/nemo-%{version}.tar.bz2
BuildRequires: libpng-devel
BuildRequires: libpng12
BuildRequires: mono-devel cairo-devel gtk-sharp2-devel gnome-sharp-devel ndesk-dbus-glib-devel
BuildRequires: udisks2
Requires: wine-mono

%description
It's a new way of managing files. Or rather not manage files.
Currently it's a cross between a calendar and a file browser with
labels. It's a free/open source GTK application written in C#.

%prep
%setup -q -n nemo-%{version}
sed -i -e 's|/usr/lib/cli|/usr/lib/mono|g' -e 's|gmcs|mcs|' Makefile
sed -i 's|Tuple|Nemo.Tuple|g' gtk/MainWindow.cs
sed -i 's|Nemo.Nemo.Tuple|Nemo.Tuple|' gtk/MainWindow.cs

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rename nemo nemodocs $RPM_BUILD_ROOT%{_bindir}/* $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/* $RPM_BUILD_ROOT%{_datadir}/applications/*
sed -i 's|nemo.exe|nemodocs.exe|' $RPM_BUILD_ROOT%{_bindir}/nemodocs
sed -i 's|=nemo|=nemodocs|' $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/*

%changelog
* Thu Feb 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.4
- Rebuild for Fedora

%undefine _debugsource_packages

Name:		gtk-theme-config
Version:	1.0
Release:	5.1
Summary:	Configure GTK theme colors
Group:		System/GUI/GNOME
License:	GPL-3.0+
URL:		https://github.com/satya164/gtk-theme-config
Source0:        gtk-theme-config-%{version}.tar.gz
BuildRequires:	glib2-devel
BuildRequires:	gtk3-devel
BuildRequires:	vala
Requires:	gsettings-desktop-schemas

%description
This little tool allows anyone to change some basic elements of a GTK theme
easily (both GTK2 and GTK3) with a simple interface.

%prep
%setup -q

%build
make

%install
make install DESTDIR=%{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%doc AUTHORS LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Tue Oct 02 2012 Satyajit Sahoo <satyajit.happy@gmail.com> 0.3
- rpm package built

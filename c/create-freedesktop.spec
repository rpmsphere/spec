Name:          create-freedesktop
Version:       0.1.3
Release:       6.2
Summary:       Shared resources for use by creative applications
Group:         Graphical Desktop/Applications/Graphics
URL:           http://create.freedesktop.org
Source:        http://create.freedesktop.org/releases/create/create-%{version}.tar.bz2
License:       GPL
BuildRequires: python2-scons <= 3.0.1
BuildArch:     noarch

%description
The Create Project provides shared resources for use by creative applications
such as Blender, CinePaint, the GIMP, Inkscape, Scribus, Audacity and the
Open Clip Art Library.

%prep
%setup -q -n create-%{version}

%build

%install
rm -rf "$RPM_BUILD_ROOT"
install -d $RPM_BUILD_ROOT%{_prefix}
scons -Q install PREFIX=$RPM_BUILD_ROOT/%{_prefix}

# remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/create/COPYING
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/create/INSTALL
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/create/spec_0.1.1.html
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/create/styles.css

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%{_datadir}/create
%doc COPYING docs/spec_0.1.1.html docs/styles.css

%changelog
* Mon Jun 13 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.3
- Rebuilt for Fedora
* Fri Nov 27 2009 Davide Madrisan <davide.madrisan@gmail.com> 0.1.3-1mamba
- package created by autospec

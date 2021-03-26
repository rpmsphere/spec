Name:           seafile
Version:        1.8.2
Release:        10.1
Summary:        File synchronization and collaboration platform for teams
License:        GPLv3
URL:            https://code.google.com/p/seafile/
Source0:        https://seafile.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  intltool
BuildRequires:  gtk2-devel
BuildRequires:  python2-devel
BuildRequires:  sqlite-devel
BuildRequires:  openssl-devel
BuildRequires:  libnotify-devel
BuildRequires:  libevent-devel
BuildRequires:  libuuid-devel
BuildRequires:  searpc-devel
BuildRequires:  ccnet-devel
BuildRequires:  vala-devel
#BuildRequires:  libzdb-devel >= 2.10
Requires:       python-mako
Requires:       python-webpy
Requires:       python-simplejson

%description
Seafile enables you to build private cloud for file sharing and collaboration
among team members in your company/organization. First you create a file library
in the web and upload files to it. Then you share it into a team or with another
user. File libraries can also be synchronized among computers and mobile devices.
You download a library to your PC. Whenever you add, delete or edit a file, the
latest version be uploaded to the server automatically and then be synchronized
to everyone's computer.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static --enable-client --disable-server
make

%install
make install DESTDIR=%{buildroot}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
sed -i 's|%{buildroot}||' %{buildroot}%{_libdir}/pkgconfig/libseafile.pc
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc LICENCE.txt README.markdown
%{_libdir}/*.so.*
%{python_sitearch}/seaserv
%{_bindir}/*
%{python_sitearch}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}/
%{_mandir}/man1/*.1.gz

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libseafile.pc

%changelog
* Wed Oct 30 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.2
- Rebuild for Fedora
* Tue Jun 18 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.7.0-1
- updated to 1.7.0
* Thu May 30 2013 Stefan Lohmaier <stefan.lohmaier@stefanlohmaier.de> - 1.1.0-1
- added description from github
- moved to seafile 1.6.1
* Mon Jan 28 2013 Robin Lee <cheeselee@fedoraproject.org> - 1.0.1-1
- Initial package

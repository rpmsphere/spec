%define debug_package %{nil}
Name:           enna-media-server
Version:        0.1
Release:        1
Summary:        media information daemon
Group:          Applications/Multimedia
License:        see COPYING
URL:            https://github.com/naguirre
Source0:        Enna-Media-Server-master.zip
# https://github.com/naguirre/Enna-Media-Server/archive/master.zip
BuildRequires:  avahi-devel
BuildRequires:  avahi-glib-devel
BuildRequires:  eio-devel
BuildRequires:  libeina-devel
BuildRequires:  eet-devel
BuildRequires:  ecore-devel
BuildRequires:  azy-devel
BuildRequires:  elementary-devel
BuildRequires:  emotion-devel 

%description
Enna Media Server, is a daemon application, which runs in background and collect informations about your medias.

%prep
%setup -q -n Enna-Media-Server-master


%build
./autogen.sh --prefix=/usr
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO
%exclude %{_bindir}/enna
%{_bindir}/enna-media-server
%{_bindir}/test_avahi_service
%{_includedir}/enna
%{_libdir}/ems
%{_libdir}/libems.*
%{_libdir}/pkgconfig/ems.pc
%{_datadir}/enna-media-server/*

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Fri Apr 26 2013  Robert Wei <robert.wei@ossii.com.tw> 0.1-1
- Port to Fedora 17


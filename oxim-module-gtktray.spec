Name:       oxim-module-gtktray
Version:    1.0
Release:    1
Summary:    the OXIM system icon tray
#Group:          
License:    GPL
#URL:            
Source0:   %{name}-%{version}.tar.gz

#BuildRequires:  
#Requires:       

%description
a system icon tray for user to use OXIM

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/oxim/modules/gtktray.so


%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Thu Nov 05 2009 Harry Chen <harry@server1.ossii.com.tw> - 1.0-1.ossii
- Initial build for osssii

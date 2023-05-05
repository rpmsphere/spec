%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build

Name:           mendeleydesktop
Version:        1.12.1
Release:        1.bin
License:        Proprietary (http://www.mendeley.com/terms/)
Summary:        A Desktop reference manager
URL:		http://www.mendeley.com/
Group:          Publishing
Source0:        %{name}-%{version}-linux-i486.tar.xz
Source1:	%{name}-%{version}-linux-x86_64.tar.xz
Source2:        mendeleydesktop_32
Source3:        mendeleydesktop_64

Provides:       libPDFNetC
Provides:       libMendeley
Requires:       %{_lib}png3
Requires:       %{_lib}qtwebkit4
Requires:       %{_lib}openssl1.0.0
Requires:       libPDFNetC
Requires:       libMendeley
BuildRequires:  desktop-file-utils
Suggests:	%{name}-integration-libreoffice

%description
Mendeley Desktop is an excellent reference manager for Windows/Mac/Linux. 
You can sync your whole library through the internet.
To activate the Mendeley Libre Office plugin open Writer and start
Tools -> Extension Manager
Click on Add..  and open the file 
/usr/share/libreoffice/share/extensions/mendeleydesktop/Mendeley-%%{version}.oxt
finally restart LibreOffice

%prep
%ifarch x86_64
%setup -q -n %{name}-%{version}-linux-x86_64 -b1
%else
%setup -q -n %{name}-%{version}-linux-i486 -b0
%endif

%build

%install
# Create Subfolders
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/libreoffice
mkdir -p %{buildroot}%{_datadir}/libreoffice/share
mkdir -p %{buildroot}%{_datadir}/libreoffice/share/extensions
mkdir -p %{buildroot}%{_datadir}/libreoffice/share/extensions/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}

#  Move Content
rm -rf lib/qt
rm bin/mendeleydesktop
%ifarch x86_64
cp %{SOURCE3} bin/mendeleydesktop
%else
cp %{SOURCE2} bin/mendeleydesktop
%endif
cp -r share/applications/* %{buildroot}%{_datadir}/applications
cp -r bin/* %{buildroot}%{_bindir}
cp -r lib/* %{buildroot}%{_libdir}
cp -r share/mendeleydesktop/openOfficePlugin/* %{buildroot}%{_datadir}/libreoffice/share/extensions/%{name}
rm -r share/mendeleydesktop/openOfficePlugin/*
cp -r share/doc/%{name}/* %{buildroot}%{_docdir}/%{name}-%{version}
rm -r share/doc/%{name}/*
cp -r share/icons/hicolor/* %{buildroot}%{_datadir}/icons/hicolor
cp -r share/%{name}/* %{buildroot}%{_datadir}/%{name}

chmod +x %{buildroot}%{_bindir}/mendeleydesktop
chmod +x %{buildroot}%{_libdir}/libPDFNetC.so
chmod +x %{buildroot}%{_libdir}/libMendeley.so.%{version}

sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_bindir}/mendeleydesktop

%clean
rm -rf %{buildroot}

%files
%dir %{_datadir}/mendeleydesktop
%dir %{_docdir}/%{name}-%{version}
%doc LICENSE README INSTALL
%{_bindir}/*
%{_libdir}/*
%{_datadir}/mendeleydesktop/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor
%{_docdir}/%{name}-%{version}/*
%dir %{_datadir}/libreoffice
%dir %{_datadir}/libreoffice/share
%dir %{_datadir}/libreoffice/share/extensions
%{_datadir}/libreoffice/share/extensions/%{name}

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.12.1
- Rebuilt for Fedora
* Tue Sep 09 2014 pinoc <vogtpet at gmail.com> 1.12.1-1pclos2014
- 1.12.1
* Thu Apr 17 2014 pinoc <vogtpet at gmail.com> 1.11-1pclos2014
- imported package
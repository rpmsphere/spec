Summary: IQ Quick Input IME Engine
Name: iqqi
Version: 1.8
Release: 5%{?dist}.bin
License: Commercial
Group: System/Internationalization
Source0: IQQI_IME_V%{version}.zip
Source1: IQQI_SDK_V%{version}_20110727.pdf
URL: http://www.iq-t.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: qt4-devel

%description
IQ Quick Input (IQQI) SDK, a smart text input solution for Win32/Linux/Android
by IQ Technology Inc.

%package devel
Summary: IQQI Header files and documents.
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}

%description devel
IQQI C develop header files.
You can learn how to use api by documents and examples.

%prep
%setup -q
cp %{SOURCE1} .
sed -i -e 's|\./IQQILibQT|%{_libdir}/IQQILibQT|' -e 's|\./Index|/usr/share/iqqi|' IQQI_IME_QT/Forms/Form_IME_KB.cpp
sed -i 's|\./Index|/usr/share/iqqi|' IQQI_IME_QT/Forms/Form_UI_*.cpp
##strip libIQQILibQT.so

%build
cd IQQI_IME_QT
qmake-qt4
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m755 libIQQILibQT.so %{buildroot}%{_libdir}
install -m644 IQQI_IME_QT/Lib/IQQI_API.h %{buildroot}%{_includedir}
cp -a Index/* %{buildroot}%{_datadir}/%{name}
chmod -R 777 %{buildroot}%{_datadir}/%{name}/*
install -m755 IQQI_IME_QT/IQQI_IME_KBD %{buildroot}%{_bindir}/%{name}-demo

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/*.so
%{_datadir}/%{name}

%files devel
%defattr(-,root,root)
%doc *.pdf IQQI_IME_QT/Lib/IQQI_API.cpp
%{_bindir}/%{name}-demo
%{_includedir}/IQQI_API.h

%changelog
* Tue Sep 13 2011 Wei-Lun Chao <bluebat@member.fsf.org> 1.8-5.bin.ossii
- Update to 1.8

* Thu May 19 2011 Wei-Lun Chao <bluebat@member.fsf.org> 1.6-1.bin.ossii
- Initial package

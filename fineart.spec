Summary: Fineart Library Hand-Written Recognition Engine
Name: fineart
Version: 20120613
Release: 1%{?dist}.bin
License: Commercial
Group: System/Internationalization
Source0: %{name}-%{version}.tar.gz
URL: http://www.fineart.com.tw
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: unzip
Provides: libFHWR.so

%description
Fineart Libray Hand-Written Recognition Engine.

%package devel
Summary: Fineart Header files and documents.
Group:          Development/Languages
Requires:       %{name}

%description devel
Fineart C develop header files.
You can learn how to use api by documents and examples.

%prep
%setup -q
%ifarch %arm
  ln -s arm lib
%else
  ln -s x86 lib
%endif

%build
make -C example

%install
rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__mkdir_p %{buildroot}%{_libdir}
%__mkdir_p %{buildroot}%{_includedir}/%{name}
%__cp example/%{name} %{buildroot}%{_bindir}/%{name}
%__cp lib/*.so %{buildroot}%{_libdir}
%__cp include/*.H %{buildroot}%{_includedir}/%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/*.so

%files devel
%defattr(-,root,root)
%doc doc/* example/*
%{_includedir}/%{name}/*

%changelog
* Mon Jun 25 2012 Wei-Lun Chao <bluebat@member.fsf.org> 20120613
- Update libraries.

* Tue Jan 10 2012 Wei-Lun Chao <bluebat@member.fsf.org> 20120110
- Update libraries.

* Thu Jun 30 2011 Chih-Chun Tu <vincent.tu@ossii.com.tw> 20110630-1.bin.ossii
- Update libraries. (FineArt-HWR-STD-arm-gcc4.2.2-20110630.zip and FineArt-HWR-STD-linux-x86-20110630.zip)

* Mon Dec 27 2010 Wei-Lun Chao <bluebat@member.fsf.org> 0.5-1.bin.ossii
- Expire on 2011-06-30

* Mon Jul 12 2010 Feather Mountain <john@ossii.com.tw> 0.4-1.bin.ossii
- Expire on 2010-12-31

* Wed Feb 03 2010 Feather Mountain <john@ossii.com.tw> 0.3-1.bin.ossii
- Update to 0.3-1

* Thu Dec 31 2009 Wei-Lun Chao <bluebat@member.fsf.org> 0.2-3.bin.ossii
- Add fineart binary

* Tue Dec 29 2009 Wei-Lun Chao <bluebat@member.fsf.org> 0.2-2.bin.ossii
- Expire on 2010-01-31

* Wed Nov 25 2009 Feather Mountain <john@ossii.com.tw> 0.2-1.bin.ossii
- New version.
- Standard CJK, support 堃﹑喆﹑煊 
 
* Tue Nov 17 2009 Feather Mountain <john@ossii.com.tw> 0.1-1.bin.ossii
- Initial package

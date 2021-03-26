Summary: Penpower Library Hand-Written Recognition Engine.
Name: penpower
Version: 0.1
Release: 4%{?dist}.bin
License: Commercial
Group: System/Internationalization
Source: penpower.tar.gz
URL: http://www.penpower.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: glibc-headers glib2

%description
Penpower Libray Hand-Written Recognition Engine API & Document.

%package devel
Summary: Penpower Header files and documents.
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}

%description devel
Penpower C develop header files.
You can learn how to use api by documents and examples.

%prep
%setup -q -n %{name}
sed -i 's|-ldl -L\.\./lib|-shared -ldl -L../x86 -fPIC|' example/Makefile

%build
LDFLAGS="%{optflags}" make -C example

%install
rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__mkdir_p %{buildroot}%{_libdir}
%__mkdir_p %{buildroot}%{_includedir}/%{name}
%__mkdir_p %{buildroot}%{_bindir}

%ifarch %arm
  %__cp arm/* %{buildroot}%{_libdir}/
%else
  %__cp x86/* %{buildroot}%{_libdir}/
%endif
%__cp share_data/* %{buildroot}%{_datadir}/%{name}/
%__cp src/* %{buildroot}%{_includedir}/%{name}/


%__cp example/penpower %{buildroot}%{_bindir}/
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root,0755)
%{_bindir}/%{name}
%{_libdir}/*.so
%{_datadir}/%{name}/*.rec
%{_datadir}/%{name}/*.dat

%files devel
%defattr(-,root,root)
%doc document/* example/*
%{_includedir}/%{name}/*.h

%changelog
* Tue Feb 02 2010 Feather Mountain <john@ossii.com.tw> 0.1-4.bin.ossii
- Add penpower.c

* Tue Jun 16 2009 Wei-Lun Chao <bluebat@member.fsf.org> 0.1-3.bin.ossii
- Add arm binary

* Tue Apr 28 2009 Feather Mountain <john@ossii.com.tw> 0.1-2.bin.ossii
- Put rec and dat files in /usr/share/penpower for penpower-python.
- Repackage.

* Fri Apr 17 2009 Feather Mountain <john@ossii.com.tw> 0.1-1.bin.ossii
- Initial package

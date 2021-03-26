Summary: VoiceText Chinese Text-To-Speech Engine
Name: voicetext
Version: 20091214
Release: 2%{?dist}.bin
License: Commercial
Group: System/Internationalization
Source: 20091214_Hui_M16_64M_x86.tar
Source1: voicetext.c
Source2: Makefile
URL: http://www.iq-t.com
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: glibc-headers
Requires: mplayer

%description
VoiceText Chinese Text-To-Speech Engine.

%package devel
Summary: VoiceText TTS Header files and documents.
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}

%description devel
VoiceText TTS C develop header files.
You can learn how to use api by documents and examples.

%prep
%setup -q -c
%__mkdir_p src
%__cp %{SOURCE1} %{SOURCE2} src/

%build
make -C src

%install
rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__mkdir_p %{buildroot}%{_libdir}
%__mkdir_p %{buildroot}%{_includedir}/%{name}
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp src/%{name} %{buildroot}%{_bindir}/%{name}
%__cp lib/* %{buildroot}%{_libdir}
%__cp include/*.h %{buildroot}%{_includedir}/%{name}
%__cp fixed_db/* %{buildroot}%{_datadir}/%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/*.so
%{_datadir}/%{name}

%files devel
%defattr(-,root,root)
%doc doc/*
%{_includedir}/%{name}/*
%{_libdir}/*.a

%changelog
* Thu Jan 28 2010 Feather Mountain <john@ossii.com.tw> 20091214-2.bin.ossii
- Add voicetext.c and Makefile

* Thu Jan 28 2010 Wei-Lun Chao <bluebat@member.fsf.org> 20091214-1.bin.ossii
- Initial package

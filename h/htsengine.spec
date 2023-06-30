%undefine _debugsource_packages

Name: htsengine
Summary: htsengine
Version: 1.05
License: BSD
Release: 1
Group: Productivity/Other
URL:https://hts-engine.sourceforge.net/
Source0: hts_engine_API-%{version}.tar.gz
Source1: hts_engine_API_reference-1.05.pdf

%description
The hts_engine is software to synthesize speech waveform from HMMs trained
by the HMM-based speech synthesis system (HTS).

%prep
%setup -q -n hts_engine_API-%{version}

%build
autoreconf -ifv
./configure
sed -i 's|-g -O2|-g -O2 -fPIC|' Makefile */Makefile
make

%install
%{__rm} -rf %{buildroot}
%{__install} -m0755 -D -s bin/hts_engine %{buildroot}/usr/bin/hts_engine
%{__install} -m0644 -D include/HTS_engine.h %{buildroot}/usr/include/HTS_engine.h
%{__install} -m0644 -D lib/libHTSEngine.a %{buildroot}%{_libdir}/libHTSEngine.a

%define docdir %{buildroot}%{_docdir}/%{name}
%{__install} -m0755 -d  %{docdir}/
%{__install} -m0644 -D AUTHORS %{docdir}/AUTHORS
%{__install} -m0644 -D COPYING  %{docdir}/COPYING
%{__install} -m0644 -D ChangeLog %{docdir}/ChangeLog
%{__install} -m0644 -D NEWS %{docdir}/NEWS
%{__install} -m0644 -D README %{docdir}/README
%{__cp} %{SOURCE1} %{docdir}/

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/hts_engine
%{_includedir}/HTS_engine.h
%{_libdir}/libHTSEngine.a
%{_docdir}/%{name}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.05
- Rebuilt for Fedora

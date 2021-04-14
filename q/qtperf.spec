%undefine _debugsource_packages

Name:           qtperf
Version:        0.2.1
Release:        20.1
License:        GPLv3
Summary:        A tool to benchmark Qt graphics performance
URL:            http://code.google.com/p/qtperf/
Group:          System/Benchmark
Source0:        http://qtperf.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  qt-devel

%description
Qtperf is an application to test Qt graphics performance. It's idea is
to draw a huge amount of predefined widgets on screen as fast as
possible while measuring time. Actually, qtperf tries to mimic
gtkperf's benchmarks, so their results should be comparable.

%prep
%setup -n %{name}

%build
qmake-qt4
make

%install
install -Dm755 qtperf4 %{buildroot}%{_bindir}/qtperf
install -Dm644 duck.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/qtperf
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1
- Rebuilt for Fedora

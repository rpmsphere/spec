Summary: A general-purpose, efficient trend graph
Name: trend
Version: 1.4
Release: 1
License: LGPL
Group: System Environment/Base
Source: trend-%{version}.tar.gz
BuildRequires: freeglut-devel libX11-devel
URL: https://www.thregr.org/wavexx/software/trend/

%description
trend is a general-purpose, efficient trend graph for "live" data. Data is
read in ASCII form from a file or continuously from a FIFO and displayed in
real-time into a multi-pass trend (much like a CRT oscilloscope). trend can
be used as a rapid analysis tool for progressive or time-based data series
together with trivial scripting.

%prep
%setup -q

%build
make -C src

%install
cd src
mkdir -p %{buildroot}/usr/{bin,share/doc/trend-%{version},share/man/man1}
cp trend %{buildroot}/usr/bin
cp ../*.rst %{buildroot}/usr/share/doc/trend-%{version}
cp -a ../examples %{buildroot}/usr/share/doc/trend-%{version}/examples
cp ../trend.1 %{buildroot}/usr/share/man/man1/

%clean
rm -rf %{buildroot}

%files
%{_bindir}/trend
%doc /usr/share/doc/trend-%{version}
%doc /usr/share/man/man1/trend.1*

%changelog
* Sun Oct 29 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
* Mon Oct 29 2007 Andras Horvath <Andras.Horvath@cern.ch> 20071027
- new upstream beta release:
-   Polling rate limits can now be configured dynamically.
-   Latency sampling now also shows maximal sync times.
-   NaNs can now be entered in the stream and highlighted.
-   Memory usage reduction (reduced in half).
-   'Z' allows to specify view limits by center and amplitude.
-   Support for multiple graphs in a single instance.
* Tue Oct 03 2006 Andras Horvath <Andras.Horvath@cern.ch> 20061003
- now with manual page!
- graph filling option (e.g. filling under the graph line)
* Thu Sep 28 2006 Andras Horvath <Andras.Horvath@cern.ch>
- initial packaging..

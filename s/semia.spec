%undefine _debugsource_packages

Summary: Semi-automated algorithm for measurement of ST levels
Name: semia
Version: 3.0.1
Release: 3.2
Source0: https://www.physionet.org/physiobank/database/ltstdb/%{name}-%{version}.tar.gz
License: GPL
URL: https://physionet.org/physiobank/database/ltstdb/semia/
Group: Applications/Engineering
BuildRequires: libX11-devel
BuildRequires: xview-devel
BuildRequires: wfdb-devel

%description
SEMIA is a tool for viewing time series of diagnostic and morphology parameters
of long-term ambulatory recordings, and ST segment annotations with their
corresponding ECG waveforms of the Long-Term ST Database (LTST DB). SEMIA was
created during the development of the LTST DB, a project supported by
Medtronic, Inc. (Minneapolis, MN, USA) and Zymed, Inc. (Camarillo, CA, USA).

%prep
%setup -q
sed -i -e 's|"semia.hlp"|"/usr/share/semia/semia.hlp"|' -e 's|"semia.opt"|"/usr/share/semia/semia.opt"|' semia_stubs.cc

%build
make

%install
rm -rf %{buildroot}
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
install -m644 %{name}.opt %{name}.hlp %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%doc HEADER.html
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Apr 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.1
- Rebuilt for Fedora

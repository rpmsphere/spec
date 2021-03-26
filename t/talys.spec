%undefine _missing_build_ids_terminate_build

Name: talys
Summary: Software for the simulation of nuclear reactions
Version: 1.6
Release: 12
Group: Applications/Engineering
License: GPL
URL: http://www.talys.eu/
Source0: ftp://ftp.nrg.eu/pub/www/%{name}/%{name}.tar
BuildRequires: compat-gcc-34-g77
NoSource: 0

%description
TALYS is software for the simulation of nuclear reactions. Many state-of-the-art
nuclear models are included to cover all main reaction mechanisms encountered in
light particle-induced nuclear reactions. TALYS provides a complete description
of all reaction channels and observables, and is user-friendly.

TALYS is a versatile tool to analyse basic microscopic experiments and to generate
nuclear data for applications. TALYS is created at NRG in Petten, the Netherlands,
and CEA in Bruyères-le-Châtel, France, and is available free of charge.

%package verify
Summary: Sample cases for TALYS
Requires: %{name}

%description verify
By running the script 'talys-verify', the sample cases are executed.

%prep
%setup -q -n %{name}
sed -i 's|/home/finux01b/akoning/talys/|/usr/share/talys/|' source/machine.f
sed -i 's|/bin/csh -f|/bin/sh|' samples/*/plot/plot
rm samples/verify
cat > %{name}-verify <<EOF
#!/bin/sh
if test -z "\$1" ; then
  echo "Usage: talys-verify 25"
  echo "Usage: talys-verify 1/a"
  echo "Usage: talys-verify 3/b diff"
  exit
elif test -z "\$2" ; then
  talys < /usr/share/talys/samples/\$1/new/input
else
  talys < /usr/share/talys/samples/\$1/new/input | diff -bitw - /usr/share/talys/samples/\$1/org/output
fi
EOF

%build
cd source
f77 -c *.f
f77 *.o -o talys

%install
install -Dm755 source/%{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a structure samples %{buildroot}%{_datadir}/%{name}
install -Dm755 %{name}-verify %{buildroot}%{_bindir}/%{name}-verify

%files
%doc LOG-1.6 README doc/*
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/structure

%files verify
%{_bindir}/%{name}-verify
%{_datadir}/%{name}/samples

%changelog
* Fri Jan 3 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6
- Initial package

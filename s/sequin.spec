Summary: A DNA Sequence Submission and Update Tool
Name: sequin
Version: 5.35
Release: 4.1
License: NCBI
Group: Applications/Bioinformatics
Source0: ftp://ftp.ncbi.nih.gov/sequin/CURRENT/sequin.linux.tar.gz
Source1: sequin.sh
Source2: ncbirc
URL: http://www.ncbi.nlm.nih.gov/Sequin/index.html
BuildRoot: %{_tmppath}/%{name}

%description
Sequin is a program designed to aid in the submission of sequences to
the GenBank, EMBL, and DDBJ sequence databases.  It is capable of
handling simple submissions which contain a single short mRNA sequence,
and complex submissions containing long sequences, multiple annotations,
segmented sets of DNA, or phylogenetic and population studies.  It was
written at the National Center for Biotechnology Information, part of
the National Library of Medicine at the National Institutes of Health.

%prep
%setup -q -c
cp %{SOURCE1} %{SOURCE2} .

%install
chmod 755 sequin asn2gb tbl2asn
mkdir -p $RPM_BUILD_ROOT%{_bindir}/sequin-%{version}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/sequin-%{version}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/sequin-%{version}/etc
mkdir -p $RPM_BUILD_ROOT%{_docdir}/sequin-%{version}/images
#mkdir -p $RPM_BUILD_ROOT%{_libdir}/sequin-%{version}/config
mkdir -p $RPM_BUILD_ROOT%{_libdir}/sequin-%{version}/errmsg
mkdir -p $RPM_BUILD_ROOT%{_libdir}/sequin-%{version}/data
install -m 755 sequin $RPM_BUILD_ROOT%{_libdir}/sequin-%{version}/sequin
install -m 755 asn2gb $RPM_BUILD_ROOT%{_bindir}/asn2gb
install -m 755 tbl2asn $RPM_BUILD_ROOT%{_bindir}/tbl2asn
install -m 755 sequin.htm $RPM_BUILD_ROOT%{_docdir}/sequin-%{version}/sequin.htm
install -m 755 images/* $RPM_BUILD_ROOT%{_docdir}/sequin-%{version}/images
#install -m 755 config/* $RPM_BUILD_ROOT%{_libdir}/sequin-%{version}/config
install -m 755 errmsg/* $RPM_BUILD_ROOT%{_libdir}/sequin-%{version}/errmsg
install -m 755 data/* $RPM_BUILD_ROOT%{_libdir}/sequin-%{version}/data

# Shell script added as /usr/bin/sequin
install -m 755 sequin.sh $RPM_BUILD_ROOT%{_bindir}/sequin
install -m 755 ncbirc $RPM_BUILD_ROOT%{_libdir}/sequin-%{version}/ncbirc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/sequin
%{_bindir}/tbl2asn
%{_bindir}/asn2gb
%{_docdir}/sequin-%{version}
%{_libdir}/sequin-%{version}

%changelog
* Fri Jun 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 5.35
- Rebuilt for Fedora

* Tue Feb 22 2005 Cymon J. Cox <cymon@duke.edu>
- Rebuild for version 5.35

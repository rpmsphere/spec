%global debug_package %{nil}

Name:           ncbi
Summary:        NCBI Software Development Toolkit
License:        Public Domain
Group:          Productivity/Scientific/Other
Version:        6.1
Release:        26.1
BuildRequires:  libXmu-devel
BuildRequires:  motif-devel
BuildRequires:  tcsh
BuildRequires:  libXft-devel, fontconfig-devel, libpng-devel, libjpeg-turbo-devel
Source:         ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/%{name}.tar.gz
Patch0:         ncbi-6.1-link-to-shared-motif.patch
Patch1:         ncbi-6.1-optflags.patch
Patch2:         ncbi-6.1-strncat-overflow.patch
Patch3:         ncbi-6.1-math-meaning.patch
Patch4:         ncbi-6.1-null-pointer.patch
Patch5:         ncbi-6.1-no-return.patch
Patch6:         ncbi-6.1-sequence-point.patch
URL:            ftp://ftp.ncbi.nih.gov/toolbox/ncbi_tools/README.htm
%define wwwblastdir /var/lib/wwwblast

%description
The NCBI Software Development Toolkit was developed for the production and
distribution of GenBank, Entrez, BLAST, and related services by NCBI.

%package blast
Summary:        Basic Local Alignment and Search Tool
Group:          Productivity/Scientific/Other
Requires:       ncbi-data

%description blast
The NCBI Basic Local Alignment Search Tool (BLAST) finds regions of
local similarity between sequences. The program compares nucleotide or
protein sequences to sequence databases and calculates the statistical
significance of matches. BLAST can be used to infer functional and
evolutionary relationships between sequences as well as help identify
members of gene families.

%package tools
Summary:        Utilities from the NCBI toolkit
Group:          Productivity/Scientific/Other
Requires:       ncbi-data

%description tools
This packages includes the binaries excluding the blast programs. 
Also contains documentation and man pages.

%package wwwblast
Summary:        Web-interface to the NCBI BLAST set of programs
Group:          Productivity/Scientific/Other
Requires:       httpd
URL:            http://www.ncbi.nlm.nih.gov/BLAST/

%description wwwblast
The wwwblast package contains a suite of standalone programs that perform 
various similarity searches using the BLAST heuristic algorithm. Similar to 
the NCBI BLAST server http://www.ncbi.nlm.nih.gov/blast/. wwwblast provides
a graphic user interface (GUI) through the use of web forms. Individual 
program takes the user inputs from the web form and returns the search result 
to a browser window. There are different web forms for different BLAST 
programs.

%package data
Summary:        NCBI toolkit data files
Group:          Productivity/Scientific/Other
BuildArch:      noarch

%description data
Data files used by programs in the NCBI toolkit.

%package devel
Summary:        NCBI toolkit header files needed for development
Group:          Development/Libraries/C and C++

%description devel
This package contains the header files required for development of software 
using the NCBI toolkit.

%prep
%setup -q -c %{name}
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6

#remove executable permissions
chmod -x ncbi/doc/blast/web_blast.pl
chmod -x ncbi/doc/fwd_check.sh
chmod -x ncbi/doc/fa2htgs/updateHtgsDoc

#remove zero-length files
cd ncbi/network/wwwblast
rm wwwblast.log psiblast.log rpsblast.log
sed -i 's:/usr/local/bin/perl:/usr/bin/perl:' config_setup.pl

%build
export CFLAGS="$RPM_OPT_FLAGS"
./ncbi/make/makedis.csh

%install
#install wwwblast *.cgi and *.REAL binaries
mkdir -p %{buildroot}/%{wwwblastdir}
cd ncbi
install -m 755 bin/*.REAL %{buildroot}/%{wwwblastdir}/
install -m 755 bin/*.cgi %{buildroot}/%{wwwblastdir}/
rm -rf bin/*.REAL
rm -rf bin/*.cgi

#all other binaries
mkdir -p %{buildroot}/%{_bindir}
install -m 755 bin/* %{buildroot}/%{_bindir}/

#devel files
mkdir -p %{buildroot}/%{_includedir}/ncbi

cd include
for m in `find . -type d`; do
	install -d -m 755 $m %{buildroot}/%{_includedir}/ncbi/$m
done

for n in `find . -type f`; do
	install -m 644 $n %{buildroot}/%{_includedir}/ncbi/$n
done
cd ..

#documentation
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 644 doc/man/*.1 %{buildroot}/%{_mandir}/man1/
rm -rf doc/man

mkdir -p %{buildroot}/%{_docdir}/ncbi-blast
install -m 644 doc/blast/* %{buildroot}/%{_docdir}/ncbi-blast/
rm -rf doc/blast

#data files
mkdir -p %{buildroot}/%{_datadir}/ncbi/data
install -m 644 data/* %{buildroot}/%{_datadir}/ncbi/data

#wwwblast
cd network/wwwblast
for j in `find . -type d`; do
    install -d -m 755 %{buildroot}/%{wwwblastdir}/$j
done

mkdir -p %{buildroot}/%{wwwblastdir}/TmpGifs

for k in `find . -type f`; do
    install -m 644 $k %{buildroot}/%{wwwblastdir}/$k;
done

cd %{buildroot}/%{wwwblastdir}/
for m in `find . -name '*.cgi'`; do 
    chmod 755 $m; 
done

chmod 755 %{buildroot}/%{wwwblastdir}/db/CDD/rpsfdb.csh
chmod 755 %{buildroot}/%{wwwblastdir}/db/CDD/make_cdd.csh
chmod 755 %{buildroot}/%{wwwblastdir}/config_setup.pl

mkdir -p %{buildroot}/%{_sysconfdir}/apache2/conf.d

cat << __EOF__ >> %{buildroot}/%{_sysconfdir}/apache2/conf.d/wwwblast.conf
Alias /blast "/var/lib/wwwblast/"

<Directory "/var/lib/wwwblast">
    Options ExecCGI
    AllowOverride None
    AddHandler cgi-script .cgi .REAL
    Order allow,deny
    Allow from all
</Directory>
__EOF__

%clean

%files blast
%{_bindir}/bl2seq
%{_bindir}/blastall
%{_bindir}/blastclust
%{_bindir}/blastpgp
%{_bindir}/copymat
%{_bindir}/fastacmd
%{_bindir}/formatdb
%{_bindir}/formatrpsdb
%{_bindir}/impala
%{_bindir}/makemat
%{_bindir}/megablast
%{_bindir}/rpsblast
%{_bindir}/seedtop
%{_docdir}/ncbi-blast

%files tools
%exclude %{_bindir}/bl2seq
%exclude %{_bindir}/blastall
%exclude %{_bindir}/blastclust
%exclude %{_bindir}/blastpgp
%exclude %{_bindir}/copymat
%exclude %{_bindir}/fastacmd
%exclude %{_bindir}/formatdb
%exclude %{_bindir}/formatrpsdb
%exclude %{_bindir}/impala
%exclude %{_bindir}/makemat
%exclude %{_bindir}/megablast
%exclude %{_bindir}/rpsblast
%exclude %{_bindir}/seedtop
%{_bindir}/*
%{_mandir}/man1/*
%doc ncbi/doc/*

%files wwwblast
%defattr(-,wwwrun,www)
%dir /etc/apache2
%dir /etc/apache2/conf.d
%config(noreplace) %{_sysconfdir}/apache2/conf.d/wwwblast.conf
%dir /var/lib/wwwblast
%config(noreplace) /var/lib/wwwblast/*.rc
%exclude /var/lib/wwwblast/Src
/var/lib/wwwblast/*

%files data
%{_datadir}/ncbi

%files devel
%{_includedir}/ncbi

%changelog
* Sat Jan 26 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 6.1
- Rebuild for Fedora
* Thu Sep  6 2012 scorot@free.fr
- add various patches to fix build erros when optflags are enabled
* Wed Sep  5 2012 scorot@free.fr
- remove xorg-x11-devel in build requirements
- add patch0 to link against shared motif instead of static one
- add patch1 to build source with %%%%optflags
* Wed Sep  5 2012 scorot@free.fr
- add xorg-x11-devel in build requirments
* Sun May 29 2011 Vimalkumar Velayudhan <vimalkumar_v@bioinformatics.org>
- Fixed permissions on wwwblast directories.
* Sat May 28 2011 Vimalkumar Velayudhan <vimalkumar_v@bioinformatics.org> 6.1-3
- Changed openmotif-libs to openmotif-devel to enable building of the *.REAL
  files required for wwwblast
* Sat Apr 23 2011 Vimalkumar Velayudhan <vimalkumar_v@bioinformatics.org> 6.1-2
- Minor changes to spec file
* Thu Aug 26 2010 Vimalkumar Velayudhan <vimalkumar_v@bioinformatics.org> 6.1-1
- Initial package created

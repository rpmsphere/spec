%global __os_install_post %{nil}

Summary: Waveform Database Software Package
Name: wfdb
Version: 10.5.24
Release: 12.3
License: GPLv2
Group: Libraries
Source: wfdb.tar.gz
URL: https://www.physionet.org/physiotools/wfdb.shtml
Requires: curl
BuildRequires: ghostscript-devel
BuildRequires: ImageMagick
BuildRequires: latex2html
BuildRequires: libcurl-devel
BuildRequires: expat-devel
BuildRequires: netpbm
BuildRequires: texlive-latex
BuildRequires: libX11-devel
BuildRequires: xview-devel
BuildRequires: libtirpc-devel
BuildRequires: rman

%prep
%setup -q
sed -i 's|WAVE=0|WAVE=1|' configure

%build
PATH=$PATH:/usr/openwin/bin ./configure --prefix=/usr --dynamic --mandir=%{_mandir}
sed -i 's|$(OPENWINHOME)/lib64|$(OPENWINHOME)/lib|' wave/Makefile
sed -i 's|-fno-stack-protector|-Wl,--allow-multiple-definition -fno-stack-protector -I/usr/include/tirpc -ltirpc|' wave/Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
%if 1 > 0
mkdir -p $RPM_BUILD_ROOT/usr
%ifarch x86_64 aarch64
mv build/lib build/lib64
%endif
mv build/help build/database build/share
cp -a build/* $RPM_BUILD_ROOT/usr
chmod +x $RPM_BUILD_ROOT%{_bindir}/* $RPM_BUILD_ROOT%{_libdir}/*
%else
cd lib
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}
install -m644 wfdb.h wfdblib.h ecgcodes.h ecgmap.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install -d $RPM_BUILD_ROOT%{_libdir}
install -m755 libwfdb.so.10.5 $RPM_BUILD_ROOT%{_libdir}
ln -sf libwfdb.so.10.5 $RPM_BUILD_ROOT%{_libdir}/libwfdb.so.10
ln -sf libwfdb.so.10 $RPM_BUILD_ROOT%{_libdir}/libwfdb.so
cd ../app
install -d $RPM_BUILD_ROOT%{_bindir}
install -m755 ann2rr bxb calsig ecgeval epicmp fir gqfuse gqpost gqrs hrstats ihr mfilt mrgann mxm nguess nst plotstm pscgen pschart psfd rdann rdsamp rr2ann rxr sampfreq sigamp sigavg signame signum skewedit snip sortann sqrs sqrs125 sumann sumstats tach time2sec wabp wfdb-config wfdbcat wfdbcollate wfdbdesc wfdbmap wfdbsignals wfdbtime wfdbwhich wqrs wrann wrsamp xform $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT/usr/lib/ps
install -m644 pschart.pro psfd.pro 12lead.pro $RPM_BUILD_ROOT%{_libdir}
cd ../convert
install -m755 a2m ad2m ahaecg2mit m2a md2a readid makeid edf2mit mit2edf rdedfann wav2mit mit2wav wfdb2mat revise ahaconvert $RPM_BUILD_ROOT%{_bindir}
cd ../data
install -d $RPM_BUILD_ROOT/usr/database
cp -a 100a.atr 100s.atr 100s.dat *.hea *list wfdbcal pipe tape $RPM_BUILD_ROOT/usr/database
ln -sf wfdbcal $RPM_BUILD_ROOT/usr/database/dbcal
cd ../fortran
install -m644 wfdbf.c $RPM_BUILD_ROOT%{_includedir}/%{name}
cd ../psd
install -m755 hrfft hrlomb hrmem hrplot plot2d plot3d coherence fft log10 lomb memse $RPM_BUILD_ROOT%{_bindir}
cd ../xml
install -m755 annxml heaxml xmlann xmlhea $RPM_BUILD_ROOT%{_bindir}
cd ../doc/wag-src
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m644 *.1 $RPM_BUILD_ROOT%{_mandir}/man1
%endif

# ---- wfdb [shared library] package ------------------------------------------

%description
The WFDB (Waveform Database) library supports creating, reading, and annotating
digitized signals in a wide variety of formats.  Input can be from local files
or directly from web or FTP servers (via the W3C's libwww).  WFDB applications
need not be aware of the source or format of their input, since input files are
located by searching a path that may include local and remote components, and
all data are transparently converted on-the-fly into a common format.  Although
created for use with physiologic signals such as those in PhysioBank
(https://www.physionet.org/physiobank/), the WFDB library supports a broad
range of general-purpose signal processing applications.

%files
%{_libdir}/libwfdb.so*

# ---- wfdb-devel package -----------------------------------------------------

%package devel
Summary: WFDB developer's toolkit
Group: Development/Libraries
URL: https://www.physionet.org/physiotools/wpg/
Requires: wfdb = %{version}

%description devel
This package includes files needed to develop new WFDB applications in C, C++,
and Fortran, examples in C and in Fortran, and miscellaneous documentation.

%files devel
%{_prefix}/share/database
%{_prefix}/include/wfdb
%doc checkpkg examples fortran lib/COPYING.LIB COPYING INSTALL MANIFEST NEWS README README.NETFILES

# ---- wfdb-app package -------------------------------------------------------

%package app
Summary: WFDB applications
Group: Applications/Scientific
URL: https://www.physionet.org/physiotools/wag/
Requires: wfdb >= %{version}

%description app
About 60 applications for creating, reading, transforming, analyzing,
annotating, and viewing digitized signals, especially physiologic signals.
Applications include digital filtering, event detection, signal averaging,
power spectrum estimation, and many others.

%files app
%{_bindir}/a2m
%{_bindir}/ad2m
%{_bindir}/ahaconvert
%{_bindir}/ahaecg2mit
%{_bindir}/ann2rr
%{_bindir}/annxml
%{_bindir}/bxb
%{_bindir}/calsig
%{_bindir}/coherence
%{_bindir}/cshsetwfdb
%{_bindir}/ecgeval
%{_bindir}/edf2mit
%{_bindir}/epicmp
%{_bindir}/fft
%{_bindir}/fir
%{_bindir}/heaxml
%{_bindir}/hrfft
%{_bindir}/hrlomb
%{_bindir}/hrmem
%{_bindir}/hrplot
%{_bindir}/ihr
%{_bindir}/log10
%{_bindir}/lomb
%{_bindir}/m2a
%{_bindir}/makeid
%{_bindir}/md2a
%{_bindir}/memse
%{_bindir}/mfilt
%{_bindir}/mit2edf
%{_bindir}/mit2wav
%{_bindir}/mrgann
%{_bindir}/mxm
%{_bindir}/nguess
%{_bindir}/nst
%{_bindir}/parsescp
%{_bindir}/plot2d
%{_bindir}/plot3d
%{_bindir}/plotstm
%{_bindir}/pscgen
%{_bindir}/pschart
%{_bindir}/psfd
%{_bindir}/rdann
%{_bindir}/rdedfann
%{_bindir}/rdsamp
%{_bindir}/readid
%{_bindir}/revise
%{_bindir}/rr2ann
%{_bindir}/rxr
%{_bindir}/sampfreq
%{_bindir}/setwfdb
%{_bindir}/sigamp
%{_bindir}/sigavg
%{_bindir}/signame
%{_bindir}/signum
%{_bindir}/skewedit
%{_bindir}/snip
%{_bindir}/sortann
%{_bindir}/sqrs
%{_bindir}/sqrs125
%{_bindir}/stepdet
%{_bindir}/sumann
%{_bindir}/sumstats
%{_bindir}/tach
%{_bindir}/time2sec
%{_bindir}/url_view
%{_bindir}/wabp
%{_bindir}/wav2mit
%{_bindir}/wfdb-config
%{_bindir}/wfdb2mat
%{_bindir}/wfdbcat
%{_bindir}/wfdbcollate
%{_bindir}/wfdbdesc
%{_bindir}/wfdbtime
%{_bindir}/wfdbwhich
%{_bindir}/wqrs
%{_bindir}/wrann
%{_bindir}/wrsamp
%{_bindir}/xform
%{_bindir}/xmlann
%{_bindir}/xmlhea
%{_libdir}/ps
%{_mandir}/man?/*
%{_bindir}/gqfuse
%{_bindir}/gqpost
%{_bindir}/gqrs
%{_bindir}/hrstats
%{_bindir}/pnwlogin
%{_bindir}/wfdbmap
%{_bindir}/wfdbsignals

# ---- wfdb-wave package ------------------------------------------------------

%package wave
Summary: Waveform Analyzer, Viewer, and Editor.
Group: X11/Applications/Science
URL: https://www.physionet.org/physiotools/wug/
Requires: wfdb >= %{version}
Requires: wfdb-app
Requires: xview >= 3.2

%description wave
WAVE provides an environment for exploring digitized signals and time series.
It provides fast, high-quality views of data stored locally or on remote
web or FTP servers, flexible control of standard and user-provided analysis
modules, efficient interactive annotation editing, and support for multiple
views on the same or different displays to support collaborative analysis and
annotation projects.  WAVE has been used to develop annotations for most of
the PhysioBank databases (https://www.physionet.org/physiobank/).

WAVE uses the XView graphical user interface.

%files wave
%{_bindir}/wave
%{_bindir}/wave-remote
%{_bindir}/wavescript
%{_prefix}/share/help/
%config %{_libdir}/wavemenu.def
%config %{_libdir}/X11/app-defaults/Wave
%doc wave/anntab

# ---- wfdb-doc package -------------------------------------------------------

%package doc
Summary: WFDB documentation.
Group: Documentation
URL: https://www.physionet.org/physiotools/manuals.shtml
BuildArch: noarch

%description doc
This package includes HTML, PostScript, and PDF versions of the WFDB
Programmer's Guide, the WFDB Applications Guide, and the WAVE User's Guide.

%files doc
%doc doc/wag doc/wpg doc/wug

%changelog
* Mon Feb 15 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 10.5.24
- Rebuilt for Fedora
* Sat Mar 12 2011 George B Moody <george@mit.edu>
- install to /usr/local, added expat-devel dependency
* Wed Oct 6 2010 George B Moody <george@mit.edu>
- added annxml, heaxml, xmlann, xmlhea
* Sun May 3 2009 George B Moody <george@mit.edu>
- moved wfdb-config from devel to apps
* Thu Feb 26 2009 George B Moody <george@mit.edu>
- added wfdb2mat
* Wed Feb 18 2009 George B Moody <george@mit.edu>
- added wfdbtime
* Wed Apr 9 2008 George B Moody <george@mit.edu>
- added rdedfann, signame, signum
* Thu May 11 2006 George B Moody <george@mit.edu>
- better solution for problems with compiled-in paths
* Wed May 10 2006 George B Moody <george@mit.edu>
- rewrote install section to solve problems with compiled-in paths
* Wed Aug 3 2005 George B Moody <george@mit.edu>
- added --dynamic to 'configure' argument list
* Wed Jun 8 2005 George B Moody <george@mit.edu>
- replaced libwww dependencies with libcurl
* Mon Mar 8 2004 George B Moody <george@mit.edu>
- added time2sec
* Wed Mar 19 2003 George B Moody <george@mit.edu>
- added --mandir to build, fixed linking in post
* Wed Dec 18 2002 George B Moody <george@mit.edu>
- split into wfdb, wfdb-devel, wfdb-app, wfdb-wave, wfdb-doc subpackages
* Sun Dec 8 2002 George B Moody <george@mit.edu>
- paths now use rpm's variables where possible

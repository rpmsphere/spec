Name:           dateutils
Version:        0.2.5
Release:        8.1
Summary:        Nifty command line date and time utilities
License:        BSD-3-Clause
Group:          Productivity/Text/Utilities
URL:            https://github.com/hroptatyr/dateutils/
Source:         %{name}-%{version}.tar.gz
BuildRequires: gperf, gengetopt, help2man

%description
Dateutils are a bunch of tools that revolve around fiddling with dates
and times in the command line with a strong focus on use cases that
arise when dealing with large amounts of financial data. Their target
market is shell scripts that need date calculations or calendar
conversions, and as such they are highly pipe-able and modeled after
their well-known cousins (e.g. dtest vs. test, or dgrep vs. grep).

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
This package contains the header and source files needed for
compiling programs using the %{name} libraries.

%prep
%setup -q

%build
autoreconf -i
%configure --docdir=%{_docdir}/%{name}-%{version}
make V=1

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_docdir}/%{name}-%{version}
%{_bindir}/*
%{_infodir}/%{name}.info*
%{_mandir}/man1/*.1.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/dateutils
%{_libdir}/libdut.a
%{_libdir}/pkgconfig/libdut.pc

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.5
- Rebuilt for Fedora
* Fri Sep 14 2012 sweet_f_a@gmx.de
- bump version 0.2.3, this is a bug fix and feature release.
  * ISO 8601 week dates are now first class objectsi
    (of type DT_YWD)
  * introduce %%rY specifier to denote years in calendars that
    deviate from the Gregorian year
  * dgrep accepts short-hand inputs (today, now, etc.) and also
    inputs as specified by -i
  * dadd'ing months and years to YMCW dates works now
  * zoneinfo files with only transitions in the past are handled
    properly (bug #10)
  * dseq with just 1 argument is working properly (story #36051287)
  * See info page examples and/or README.
* Fri Jul 20 2012 sweet_f_a@gmx.de
- bump version 0.2.2, this is a bug fix and feature release.
  * Olson's zoneinfo database files are checked for at configure
    time
  * leap-aware calculations use shipped leapseconds file
  * ddiff and dadd can take leap-second transitions into account
  * issue 7: ddiff without arguments does not segfault
  * issue 8: dadd copes with huge summands
  * issue 9: dadd stumbles on ymcw dates
  * bug 33104651: bday negative difference A > B ddiff A B -f %%db
    is wrong
  * See info page examples and/or README.
* Tue Jun 19 2012 sweet_f_a@gmx.de
- bump version 0.2.1, this is a bug fix and feature release.
  * The dadd tool now supports mass-adding durations (from stdin).
  * The ddiff tool is now time zone aware.
  * A new tool dround is added to round dates or times or
    date-times to the next occurrence of what's given as
    round-spec.
  * Bug fixes:
  - issue 7: ddiff without arguments does not segfault
  - issue 8: dadd copes with huge summands
  * See info page examples and/or README.
* Tue Apr 10 2012 sweet_f_a@gmx.de
- bump version 0.2.0, this is a feature release.
  * The distinction between binaries for date, time and date-time
    processing is cleared up by a unified set of tools, prefixed
    with `d'.
    Thus:
    dadd + tadd -> dadd
    dconv + tconv + dtconv -> dconv
    ddiff + tdiff -> ddiff
    dgrep + tgrep -> dgrep
    dseq + tseq -> dseq
    dtest + ttest -> dtest
  * Furthermore, all tools now fully cope with dates, times and
    date-times.
  * Virtual timezones have been added (use `GPS' or `TAI').
  * See info page examples and/or README.
* Fri Mar 23 2012 sweet_f_a@gmx.de
- bump version 0.1.10, this is a bug fix release.
  * account for big-endian machines
  * GNUisms (mempcpy() and getline()) are removed
  * inf-loop in tseq is fixed (bug #6)
  * nanoseconds are preserved upon time zone conversion
- add byteswap.patch to fix build for old distros
* Wed Feb  1 2012 sweet_f_a@gmx.de
- bump version 0.1.9, this is a bug fix release.
  * The code for date addition is refactored, with it a new
    duration type is introduced, DT_MD, to capture larger month and
    day summands.
* Tue Jan  3 2012 sweet_f_a@gmx.de
- bump version 0.1.8, this is a bug fix release.
  * A bit fiddling bug gave erroneous results in `dconv now'.
  * Furtherly, date expressions (for dgrep et al.) can now be
    arbitrarily joined with conjunctions (&&) and disjunctions (||)
    as well as negations (!).
* Thu Oct 27 2011 sweet_f_a@gmx.de
- bump version 0.1.7, this is a bug fix release.
* Fri Oct 21 2011 sweet_f_a@gmx.de
- bump version 0.1.6
* Wed Sep 14 2011 sweet_f_a@gmx.de
- initial package datetools 0.1.2

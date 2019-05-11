#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sfsmisc
Version  : 1.1.4
Release  : 26
URL      : https://cran.r-project.org/src/contrib/sfsmisc_1.1-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sfsmisc_1.1-4.tar.gz
Summary  : Utilities from Seminar fuer Statistik ETH Zurich
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Hmisc
Requires: R-e1071
BuildRequires : R-Hmisc
BuildRequires : R-e1071
BuildRequires : buildreq-R

%description
sfsmisc
=======
The R package sfsmisc  has finally made it into a revision control system,
and the fad of the day being git & github, so be it!

%prep
%setup -q -c -n sfsmisc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557588044

%install
export SOURCE_DATE_EPOCH=1557588044
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sfsmisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sfsmisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sfsmisc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc sfsmisc || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sfsmisc/ChangeLog
/usr/lib64/R/library/sfsmisc/DESCRIPTION
/usr/lib64/R/library/sfsmisc/INDEX
/usr/lib64/R/library/sfsmisc/Meta/Rd.rds
/usr/lib64/R/library/sfsmisc/Meta/data.rds
/usr/lib64/R/library/sfsmisc/Meta/demo.rds
/usr/lib64/R/library/sfsmisc/Meta/features.rds
/usr/lib64/R/library/sfsmisc/Meta/hsearch.rds
/usr/lib64/R/library/sfsmisc/Meta/links.rds
/usr/lib64/R/library/sfsmisc/Meta/nsInfo.rds
/usr/lib64/R/library/sfsmisc/Meta/package.rds
/usr/lib64/R/library/sfsmisc/NAMESPACE
/usr/lib64/R/library/sfsmisc/NEWS.Rd
/usr/lib64/R/library/sfsmisc/R/sfsmisc
/usr/lib64/R/library/sfsmisc/R/sfsmisc.rdb
/usr/lib64/R/library/sfsmisc/R/sfsmisc.rdx
/usr/lib64/R/library/sfsmisc/data/potatoes.rda
/usr/lib64/R/library/sfsmisc/demo/hatmat-ex.R
/usr/lib64/R/library/sfsmisc/demo/pretty-lab.R
/usr/lib64/R/library/sfsmisc/demo/prime-numbers.R
/usr/lib64/R/library/sfsmisc/help/AnIndex
/usr/lib64/R/library/sfsmisc/help/aliases.rds
/usr/lib64/R/library/sfsmisc/help/paths.rds
/usr/lib64/R/library/sfsmisc/help/sfsmisc.rdb
/usr/lib64/R/library/sfsmisc/help/sfsmisc.rdx
/usr/lib64/R/library/sfsmisc/html/00Index.html
/usr/lib64/R/library/sfsmisc/html/R.css
/usr/lib64/R/library/sfsmisc/tests/dDA.R
/usr/lib64/R/library/sfsmisc/tests/dDA.Rout.save
/usr/lib64/R/library/sfsmisc/tests/eaxis.R
/usr/lib64/R/library/sfsmisc/tests/misc.R
/usr/lib64/R/library/sfsmisc/tests/p.R
/usr/lib64/R/library/sfsmisc/tests/p.Rout.save
/usr/lib64/R/library/sfsmisc/tests/posdef.R
/usr/lib64/R/library/sfsmisc/tests/posdef.Rout.save

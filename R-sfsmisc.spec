#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 5424026
#
Name     : R-sfsmisc
Version  : 1.1.20
Release  : 71
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/sfsmisc_1.1-20.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/sfsmisc_1.1-20.tar.gz
Summary  : Utilities from 'Seminar fuer Statistik' ETH Zurich
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
some of which were ported from S-plus in the 1990s.
 For graphics, have pretty (Log-scale) axes eaxis(), an enhanced Tukey-Anscombe
   plot, combining histogram and boxplot, 2d-residual plots, a 'tachoPlot()',
   pretty arrows, etc.
 For robustness, have a robust F test and robust range().
 For system support, notably on Linux, provides 'Sys.*()' functions with
   more access to system and CPU information.
 Finally, miscellaneous utilities such as simple efficient prime numbers,
   integer codes, Duplicated(), toLatex.numeric() and is.whole().

%prep
%setup -q -n sfsmisc
pushd ..
cp -a sfsmisc buildavx2
popd
pushd ..
cp -a sfsmisc buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731651006

%install
export SOURCE_DATE_EPOCH=1731651006
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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

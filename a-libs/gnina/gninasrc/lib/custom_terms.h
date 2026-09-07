/* GPL 2.0
 * Copyright 2012 David Koes and University of Pittsburgh
 *
 * This implements a customizable scoring function class that can be
 * initialized using a user provided file.
 */
#ifndef SMINA_CUSTOM_TERMS_H
#define SMINA_CUSTOM_TERMS_H

#include "terms.h"
#include "int_pow.h"
#include "everything.h"
#include <string>
#include <boost/regex.hpp>
#include "file.h"

//terms that can be dynamically built
//also, keeps track of weights (in right order)
struct custom_terms : public terms {
  private:
    //weights must match type-specific ordering of terms
    flv term_weights[LastTermKind];
    term_creators creators;
    fl scaling_factor;

  public:
    custom_terms() {
      scaling_factor = 1;
    }
    void add(const std::string& name, fl weight);
    flv weights() const;
    void add_terms_from_file(std::istream& in);
    void print(std::ostream& out) const;

    void print_available_terms(std::ostream& out) const;
    friend std::ostream& operator<<(std::ostream& out, const custom_terms& t);
    void set_scaling_factor(fl sf);

    //add the standard Vina scoring terms
    void add_vina() {
      add("gauss(o=0,_w=0.5,_c=8)", -0.035579);
      add("gauss(o=3,_w=2,_c=8)", -0.005156);
      add("repulsion(o=0,_c=8)", 0.840245);
      add("hydrophobic(g=0.5,_b=1.5,_c=8)", -0.035069);
      add("non_dir_h_bond(g=-0.7,_b=0,_c=8)", -0.587439);
      add("num_tors_div", 5 * 0.05846 / 0.1 - 1);
    }
};

#endif
